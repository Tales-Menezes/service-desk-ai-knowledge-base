import os
from flask import Blueprint, request, redirect
from app.services.ingestion_service import prepare_documents
from app.services.search_index_service import SearchIndexService
from app.services.search_service_factory import get_search_service

upload_bp = Blueprint("upload", __name__)
@upload_bp.route("/upload", methods=["POST"])

def upload():
    file = request.files["file"]
    client = request.form["client"]
    category = request.form["category"]

    file_path = f"/tmp/{file.filename}"

    try:
        file.save(file_path)

        documents = prepare_documents(
            file_path=file_path,
            client=client,
            category=category,
            title=file.filename,
            source_file=file.filename
        )

        search_service = get_search_service()
        search_service.upload_chunks(documents)
    finally:
        # Ensure the temporary file is removed after processing
        if os.path.exists(file_path):
            os.remove(file_path)

    return redirect("/")
