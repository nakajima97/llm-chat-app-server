from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from src.clients.openai_client import get_openai_client


def generate_title(user_message: str):
    """
    OpenAIのGPT-4o-miniを使ってスレッドのタイトルを生成する
    """
    # OpenAIのモデルのインスタンスを作成
    llm = get_openai_client()

    # チャットメッセージを文字列に変換するための出力解析インスタンスを作成
    output_parser = StrOutputParser()

    # プロンプトの生成
    prompt = ChatPromptTemplate(
        [
            (
                "system",
                "次のユーザ(user)とLLMの回答(assistant)のやり取りに20文字以内でタイトルをつけてください。メッセージは次の形式で来ます: user=今日の天気は？",
            ),
            ("user", "user={user_message}"),
        ]
    )

    # OpenAIのAPIにこのプロンプトを送信するためのチェーンを作成
    chain = prompt | llm | output_parser

    return chain.invoke({"user_message": user_message})
