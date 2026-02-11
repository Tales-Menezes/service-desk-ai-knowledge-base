from PyPDF2 import PdfReader
from docx import Document

# Simple text extraction service that supports PDF, DOCX, TXT, and MD files.
def extract_text(file_path: str) -> str:

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)
    
    if file_path.endswith(".txt") or file_path.endswith(".md"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
        
    raise ValueError("Unsupported file type")
