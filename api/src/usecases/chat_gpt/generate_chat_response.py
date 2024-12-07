from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from src.services.openai_service import get_chat_model


def generate_chat_response(sentence):
    """
    OpenAIのGPT-4o-miniを使って文章を生成する
    """
    # OpenAIのモデルのインスタンスを作成
    llm = get_chat_model()

    # チャットメッセージを文字列に変換するための出力解析インスタンスを作成
    output_parser = StrOutputParser()

    # プロンプトの生成
    prompt = ChatPromptTemplate.from_messages([("user", sentence)])

    # OpenAIのAPIにこのプロンプトを送信するためのチェーンを作成
    chain = prompt | llm | output_parser

    # チェーンを実行し、結果を返す
    return chain.invoke({})
