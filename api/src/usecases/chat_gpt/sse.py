import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from src.config import Config



# astreamを用いてストリームする
async def stream_generate(question: str):
    """
    OpenAIのGPT-4o-miniを使って文章をstreamで生成する
    """

    # チャットモデルのインスタンスを作成
    model = ChatOpenAI(openai_api_key=Config.OPENAI_API_KEY, model="gpt-4o-mini")

    # プロンプトのテンプレート文章を定義
    prompt = ChatPromptTemplate.from_template("{question}")

    # 出力パーサーを定義
    parser = StrOutputParser()

    # プロンプトとモデル、パーサーをチェーン化する
    chain = prompt | model | parser

    # astreamでストリーミングを開始
    async for chunk in chain.astream({"question": question}):
        # 出力結果をコンソールに出力
        yield chunk
