from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

class SearchIndexService:
    """Handles indexing documents into Cognitive Search."""

    def __init__(self):
        self.client = SearchClient(
            endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
            index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
            credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_ADMIN_KEY"))
        )

    def upload_chunks(self, documents: list):
        self.client.upload_documents(documents)
