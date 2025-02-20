import os
from dotenv import load_dotenv

load_dotenv()


class Env:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    CORS_ORIGIN = os.environ.get("CORS_ORIGIN")
    DB_HOST = os.environ.get("DB_HOST")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_NAME = os.environ.get("DB_NAME")
    DB_PORT = os.environ.get("DB_PORT")
    CHROMA_HOST = os.environ.get("CHROMA_HOST")
    CHROMA_PORT = os.environ.get("CHROMA_PORT")
    CHROMA_SSL = os.environ.get("CHROMA_SSL")
