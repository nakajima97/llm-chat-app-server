from langchain_openai import ChatOpenAI
from src.configs.config import Config


def get_openai_client():
    return ChatOpenAI(
        openai_api_key=Config.OPENAI_API_KEY, model_name="gpt-4o-mini", temperature=0
    )
