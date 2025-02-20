from langchain_openai import ChatOpenAI
from src.configs.env import Env


def get_openai_client():
    return ChatOpenAI(
        openai_api_key=Env.OPENAI_API_KEY, model_name="gpt-4o-mini", temperature=0
    )
