from src.clients.chroma_service import get_chroma_client


def query_chroma(query: str, count: int = 3):
    vector_store = get_chroma_client()

    results = vector_store.similarity_search(
        query,
        k=count,
    )

    result_list = [doc.page_content for doc in results]

    return result_list
