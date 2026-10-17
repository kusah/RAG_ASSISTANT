from app.services.embedding_service import generate_embeddings


chunks = [
    "Database normalization reduces data redundancy.",
    "A primary key uniquely identifies a record.",
    "SQL is used to query relational databases."
]

embeddings = generate_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)