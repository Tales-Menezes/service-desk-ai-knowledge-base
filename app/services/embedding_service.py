import os
from typing import List
from openai import AzureOpenAI


EMBEDDING_DIMS = 1536

class EmbeddingService:
    def __init__(self) -> None:
        self.enabled = (os.getenv("EMBEDDING_ENABLED", "false").lower() == "true")

        if not self.enabled:
            self.client = None
            self.deployment = None
            return
        
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key = os.getenv("AZURE_OPENAI_API_KEY"),
        api_version = os.getenv("AZURE_OPENAI_API_VERSION")
                
        if not endpoint or not api_key or not api_version:
            raise RuntimeError(
                "Azure Search env vars missing (AZURE_OPENAI_ENDPOINT / "
                "AZURE_OPENAI_API_KEY / AZURE_OPENAI_API_VERSION)."
            )
        
        self.client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version,
        )

        self.deployment = os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT"]

    def embed(self, text: str) -> list[float]:
        if not self.enabled:
            return []

        text = (text or "").strip()
        if not text:
            return [0.0] * EMBEDDING_DIMS

        resp = self.client.embeddings.create(
            model=self.deployment,
            input=text
        )
        return resp.data[0].embedding
