import json
import os
from typing import List, Dict, Any

class MockSearchQueryService:
    def __init__(self, storage_path: str = "/tmp/mock_index.json"):
        self.storage_path = storage_path
    
    def search(self, query: str, client: str = None, top: int = 5) -> List[Dict[str, Any]]:
        if not os.path.exists(self.storage_path):
            return []
        
        with open(self.storage_path, 'r', encoding = "utf-8") as f:
            docs = json.load(f)
        
        q = (query or "").lower().strip()
        results = []

        for d in docs:
            if client and d.get("client") != client:
                continue
            hay = (d.get("content") or "").lower()
            title = (d.get("title") or "").lower()
            cat = (d.get("category") or "").lower()

            # Simple relevance: count occurrences accross fields
            score = hay.count(q) + title.count(q) + cat.count(q)
            if q and q not in hay and q not in title and q not in cat:
                continue

            d["_score"] = score
            results.append(d)
        
        results.sort(key=lambda x: x.get("_score",0), reverse=True)
        return results[:top]
        
