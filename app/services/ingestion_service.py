import uuid
from app.services.text_extraction_service import extract_text
from app.services.chunking_service import chunk_text

#Converts a knowledge base file into search-indexable document chunks.
def prepare_documents(
    file_path: str,
    client: str,
    category: str,
    title: str,
    source_file: str
): 
    text = extract_text(file_path)
    chunks = chunk_text(text)

    documents = []
    for index, chunk in enumerate(chunks):
        documents.append({
            "id": f"{uuid.uuid4()}",
            "content": chunk,
            "client": client,
            "category": category,
            "title": title,
            "source_file": source_file,
            "chunk_index": index
        })

    return documents