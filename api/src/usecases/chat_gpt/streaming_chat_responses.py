from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from src.services.openai_service import get_chat_model


# astreamを用いてストリームする
async def streaming_chat_responses(messages: list):
    """
    OpenAIのGPT-4o-miniを使って文章をstreamで生成する
    """

    # チャットモデルのインスタンスを作成
    model = get_chat_model()

    # プロンプトのテンプレート文章を定義
    prompt = ChatPromptTemplate.from_messages(messages)

    # 出力パーサーを定義
    parser = StrOutputParser()

    # プロンプトとモデル、パーサーをチェーン化する
    chain = prompt | model | parser

    # astreamでストリーミングを開始
    async for chunk in chain.astream({}):
        # 出力結果をコンソールに出力
        yield chunk
