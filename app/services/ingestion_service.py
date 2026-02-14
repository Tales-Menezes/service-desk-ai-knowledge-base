import uuid
import os
from app.services.text_extraction_service import extract_text
from app.services.chunking_service import chunk_text
from app.services.embedding_service import EmbeddingService

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
    backend = os.getenv("SEARCH_BACKEND", "mock").lower()
    if backend == "azure":
        embedder = EmbeddingService()
        for doc in documents:
            if embedder.enabled:
                doc["embedding"] = embedder.embed(doc["content"])
    
    return documents