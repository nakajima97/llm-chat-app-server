import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def chat_gpt(sentence):
    '''
    OpenAIのGPT-4o-miniを使って文章を生成する
    '''
    # OpenAIのモデルのインスタンスを作成
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-4o-mini", temperature=0)

    # チャットメッセージを文字列に変換するための出力解析インスタンスを作成
    output_parser = StrOutputParser()

    # プロンプトの生成
    prompt = ChatPromptTemplate.from_messages([
        ("user", sentence)
    ])

    # OpenAIのAPIにこのプロンプトを送信するためのチェーンを作成
    chain = prompt | llm | output_parser

    # チェーンを実行し、結果を返す
    return chain.invoke({})