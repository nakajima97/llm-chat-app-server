import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# チャットモデルのインスタンスを作成
model = ChatOpenAI(model="gpt-4o-mini")

# プロンプトのテンプレート文章を定義
prompt = ChatPromptTemplate.from_template("質問に回答してください")

# 出力パーサーを定義
parser = StrOutputParser()

# astreamを用いてストリームする
async def stream_generate():
    # プロンプトとモデル、パーサーをチェーン化する
    chain = prompt | model | parser

    # 質問を指定
    question = "東京の天気は？"

    # astreamでストリーミングを開始
    async for chunk in chain.astream({"question": question}):
        # 出力結果をコンソールに出力
      yield chunk