from langchain_openai import OpenAIEmbeddings
from chromadb import HttpClient
from src.config import Config
from langchain_chroma import Chroma


def get_chroma_client():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
        client=HttpClient(
            host=Config.CHROMA_HOST,
            port=Config.CHROMA_PORT,
            ssl=Config.CHROMA_SSL.lower() == "true",
        ),
    )

    return vector_store
