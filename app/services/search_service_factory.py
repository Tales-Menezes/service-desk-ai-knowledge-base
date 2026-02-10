import os

def get_search_service():
    backend = os.getenv("SEARCH_BACKEND", "azure").lower()

    if backend == "mock":
        from app.services.mock_search_index_service import MockSearchIndexService
        return MockSearchIndexService()

    from app.services.search_index_service import SearchIndexService
    return SearchIndexService()
