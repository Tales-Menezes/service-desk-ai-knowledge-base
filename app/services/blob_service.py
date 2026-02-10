from azure.storage.blob import BlobServiceClient
import os

class BlobStorageService:
    """Handles uploads to Azure Blob Storage."""

    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        )

    def upload_file(self, container: str, file_path: str, blob_name: str):
        container_client = self.client.get_container_client(container)
        with open(file_path, "rb") as data:
            container_client.upload_blob(blob_name, data, overwrite=True)