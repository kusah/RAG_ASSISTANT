from app.services.retrieval_service import search_similar_chunks


query = "Why do we normalize databases?"

results = search_similar_chunks(query)

print("Retrieved chunks:")

for chunk in results["documents"][0]:
    print("-", chunk)