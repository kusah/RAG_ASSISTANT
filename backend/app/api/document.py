import os
import shutil
import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.crud.document import create_document
from app.database.database import get_db
from app.models.user import User
from app.schemas.document import DocumentResponse
from app.services.rag_service import process_document


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload", response_model=DocumentResponse)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # 1. Validate file
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # 2. Get extension
    file_extension = os.path.splitext(file.filename)[1]

    # 3. Generate unique filename
    unique_filename = f"{uuid.uuid4()}{file_extension}"

    # 4. Create upload directory
    upload_dir = "app/uploads/pdfs"
    os.makedirs(upload_dir, exist_ok=True)

    # 5. Create file path
    file_path = os.path.join(
        upload_dir,
        unique_filename
    )

    # 6. Save PDF
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 7. Create database record
        document = create_document(
            db=db,
            filename=file.filename,
            filepath=file_path,
            user_id=current_user.id,
        )

        # 8. Process PDF for RAG
        process_document(
            file_path=file_path,
            document_id=document.id
        )

    except Exception as e:
        # Remove uploaded file if processing fails
        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=500,
            detail=f"Failed to process document: {str(e)}"
        )

    return document