import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    CORS_ORIGIN = os.environ.get("CORS_ORIGIN")
