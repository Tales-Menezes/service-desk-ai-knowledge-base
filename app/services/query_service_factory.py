import os

def get_query_service():
    backend = os.getenv("SEARCH_BACKEND", "mock").lower()

    if backend == "mock":
        from app.services.mock_search_query_service import MockSearchQueryService
        return MockSearchQueryService()
    
    if backend == "azure":
        from app.services.azure_search_query_service import AzureSearchQueryService
        return AzureSearchQueryService()
    
    # Placeholder: Step 5 will add Azure quesry service
    raise RuntimeError(f"Unknown SEARCH_BACKEND {backend}")