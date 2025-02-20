from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from src.clients.openai_service import get_chat_model
from src.repositories.query_chroma import query_chroma
from langchain.schema import HumanMessage


# astreamを用いてストリームする
async def streaming_chat_responses(histories: list, question: str):
    """
    OpenAIのGPT-4o-miniを使って文章をstreamで生成する
    """
    result = query_chroma(question)
    context = "\n".join(result)

    # チャットモデルのインスタンスを作成
    model = get_chat_model()

    histories.append(
        HumanMessage(
            content=f"""
以下の文脈をもとに質問に回答してください

{context}

質問: {question}
"""
        )
    )

    # プロンプトのテンプレート文章を定義
    prompt = ChatPromptTemplate.from_messages(histories)

    # 出力パーサーを定義
    parser = StrOutputParser()

    # プロンプトとモデル、パーサーをチェーン化する
    chain = prompt | model | parser

    # astreamでストリーミングを開始
    async for chunk in chain.astream({}):
        # 出力結果をコンソールに出力
        yield chunk
