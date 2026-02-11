import os
from PyPDF2 import PdfReader
from docx import Document

def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if ext == ".docx":
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    if ext in {".txt", ".md"}:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()

    raise ValueError(f"Unsupported file type: {ext}")
