import os
import tempfile
from pathlib import Path

from flask import Blueprint, request, redirect
from app.services.ingestion_service import prepare_documents
from app.services.search_index_service import SearchIndexService
from app.services.search_service_factory import get_search_service
from werkzeug.utils import secure_filename # Sanitize file names for security

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    client = request.form["client"]
    category = request.form["category"]

    temp_dir = Path(os.getenv("APP_TEMP_DIR", tempfile.gettempdir()))
    temp_dir.mkdir(parents=True, exist_ok=True)

    filename = secure_filename(file.filename) # Sanitize the file name

    file_path = temp_dir / filename

    try:
        file.save(str(file_path))

        documents = prepare_documents(
            file_path=str(file_path),
            client=client,
            category=category,
            title=filename,
            source_file=filename
        )

        search_service = get_search_service()
        search_service.upload_chunks(documents)
    finally:
        # Ensure the temporary file is removed after processing
        if file_path.exists():
            file_path.unlink()

    return redirect("/search")
