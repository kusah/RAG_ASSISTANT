from app.services.pdf_service import extract_text_from_pdf

file_path = r"D:\rag-knowledge-assistant\backend\app\uploads\pdf\BBIT417P_Assessment1.pdf"

text = extract_text_from_pdf(file_path)

print("Extracted text:")
print(text)