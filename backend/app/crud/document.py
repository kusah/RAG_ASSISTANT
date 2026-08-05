from sqlalchemy.orm import Session

from app.models.document import Document


def create_document(
    db: Session,
    filename: str,
    filepath: str,
    user_id: int,
):
    document = Document(
        filename=filename,
        filepath=filepath,
        user_id=user_id,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document