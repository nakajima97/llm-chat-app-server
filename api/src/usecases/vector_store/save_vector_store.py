from src.repositories.save_chroma import save_chroma


def save_vector_store(text: str):
    save_chroma(text)