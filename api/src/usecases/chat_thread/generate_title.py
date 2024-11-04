from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from src.services.openai_service import get_chat_model


def generate_title(user_message: str, assistant_message: str):
    """
    OpenAIのGPT-4o-miniを使ってスレッドのタイトルを生成する
    """
    # OpenAIのモデルのインスタンスを作成
    llm = get_chat_model()

    # チャットメッセージを文字列に変換するための出力解析インスタンスを作成
    output_parser = StrOutputParser()

    # プロンプトの生成
    prompt = ChatPromptTemplate(
        [
            (
                "system",
                "次のユーザ(user)とLLMの回答(assistant)のやり取りに20文字以内でタイトルをつけてください。メッセージは次の形式で来ます: user=今日の天気は？, assistant=今日の天気は晴れです。",
            ),
            ("user", "user={user_message}, assistant={assistant_message}"),
        ]
    )

    # OpenAIのAPIにこのプロンプトを送信するためのチェーンを作成
    chain = prompt | llm | output_parser

    return chain.invoke(
        {"user_message": user_message, "assistant_message": assistant_message}
    )
