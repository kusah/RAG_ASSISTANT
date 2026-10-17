from app.services.chunking_service import chunk_text

text = "This is a test document. " * 500

chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}")
    print(chunk[:100])