from app.services.embedding_service import generate_embeddings
from app.services.vector_store import add_chunks


chunks = [
    "Database normalization reduces data redundancy.",
    "A primary key uniquely identifies a record.",
    "SQL is used to query relational databases."
]

embeddings = generate_embeddings(chunks)

add_chunks(
    chunks=chunks,
    embeddings=embeddings,
    document_id=1
)

print("Chunks successfully stored in ChromaDB!")