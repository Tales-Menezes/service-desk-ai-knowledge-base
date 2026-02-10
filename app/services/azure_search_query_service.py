import os
from typing import List, Dict, Any
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

class AzureSearchQueryService:
    def __init__(self):
        endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
        admin_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
        if not endpoint or not index_name or not admin_key:
            raise RuntimeError("Azure Search env vars missing (endpoint/index/key).")

        self.client = SearchClient(
            endpoint=endpoint,
            index_name=index_name,
            credential=AzureKeyCredential(admin_key)
        )

    def search(self, query: str, client: str = None, top: int = 5) -> List[Dict[str, Any]]:
        filter_expr = None
        if client:
            safe_client = client.replace("'", "''")
            filter_expr = f"client eq '{safe_client}'"

        results = self.client.search(
            search_text=query or "*",
            filter=filter_expr,
            top=top,
            select=["id", "title", "content", "client", "category", "source_file", "chunk_index"],
        )

        out = []
        for r in results:
            d = dict(r)
            d["_score"] = d.get("@search.score", 0)
            out.append(d)
        return out
