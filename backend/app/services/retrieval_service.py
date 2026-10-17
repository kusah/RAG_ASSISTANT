from app.services.vector_store import collection
from app.services.embedding_service import generate_embeddings


def search_similar_chunks(
    query: str,
    top_k: int = 3
):
    query_embedding = generate_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k
    )

    return results