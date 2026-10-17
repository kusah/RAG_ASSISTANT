from app.services.llm_service import generate_answer

answer = generate_answer(
    query="What is normalization?",
    context="""
    Database normalization is the process of organizing
    data in a relational database to reduce redundancy
    and improve data integrity.
    """
)

print(answer)