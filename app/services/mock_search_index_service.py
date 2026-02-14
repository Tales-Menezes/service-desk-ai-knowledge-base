import json
import os
import tempfile
from pathlib import Path
from typing import List, Dict, Any

class MockSearchIndexService:
    """
    Local stand-in for Azure Cognitive Search.
    Stores uploaded chunks to a JSON file so we can test ingestion end-to-end.
    """

    def __init__(self, storage_path: str | None = None ):
        default_path = Path(os.getenv("APP_TEMP_DIR", tempfile.gettempdir())) / "mock_index.json"
        self.storage_path = str(storage_path or default_path)

    def upload_chunks(self, documents: List[Dict[str, Any]]) -> None:
        existing = []
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as f:
                existing = json.load(f)

        existing.extend(documents)

        Path(self.storage_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
