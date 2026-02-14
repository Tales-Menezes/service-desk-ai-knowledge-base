from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

class SearchIndexService:
    """Handles indexing documents into Cognitive Search."""

    def __init__(self):
        endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
        index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
        admin_key=os.getenv("AZURE_SEARCH_ADMIN_KEY")
                
        if not endpoint or not index_name or not admin_key:
            raise RuntimeError(
                "Azure Search env vars missing (AZURE_SEARCH_ENDPOINT / "
                "AZURE_SEARCH_INDEX_NAME / AZURE_SEARCH_ADMIN_KEY)."
            )
        
        self.client = SearchClient(
            endpoint=endpoint,
            index_name=index_name,
            credential=AzureKeyCredential(admin_key),
        )

    def upload_chunks(self, documents: list):
        results = self.client.upload_documents(documents)
        failed = [r for r in results if not r.succeeded]
        if failed:
            raise RuntimeError(f"{len(failed)} documents failed to index: {failed[:3]}")
        self.client.upload_documents(documents)
