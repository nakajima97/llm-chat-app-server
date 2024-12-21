from src.services.chroma import get_chroma_client

def query_chroma(query: str, count: int = 3):
    vector_store = get_chroma_client()

    results = vector_store.similarity_search(
        query,
        k=count,
    )

    result_list = [
        {"content": doc.page_content, "relevance_score": score}
        for doc, score in results
    ]

    return result_list
