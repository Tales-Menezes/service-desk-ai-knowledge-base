import os

def get_query_service():
    backend = os.getenv("SEARCH_BACKEND", "azure").lower()

    if backend == "mock":
        from app.services.mock_search_query_service import MockSearchQueryService
        return MockSearchQueryService()
    
    # Placeholder: Step 5 will add Azure quesry service
    raise RuntimeError("Azure query backend not configured yet. Set SEARCH_BACKEND=mock for local testing.")