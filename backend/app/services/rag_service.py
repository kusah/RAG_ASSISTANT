from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.vector_store import add_chunks


def process_document(
    file_path: str,
    document_id: int
):
    text = extract_text_from_pdf(file_path)

    if not text.strip():
        raise ValueError("PDF contains no extractable text.")

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    add_chunks(
        chunks=chunks,
        embeddings=embeddings,
        document_id=document_id
    )

    return {
        "chunks": len(chunks)
    }