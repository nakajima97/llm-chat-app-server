import logging
from uuid import uuid4
from langchain_core.documents import Document
from src.clients.chroma_service import get_chroma_client

# ロギングの設定
logging.basicConfig(level=logging.INFO)


def save_chroma(content: str):
    """
    与えられたテキストをChromaDBに保存する関数。

    Args:
        content: 保存するテキスト。
    Returns:
        成功すればUUID, 失敗すればNone
    """
    try:
        vector_store = get_chroma_client()

        # UUID を1つだけ生成して再利用
        document_id = str(uuid4())
        document = Document(
            page_content=content,
            metadata={"source": "save_chroma"},
            id=document_id,
        )

        vector_store.add_documents(
            documents=[document], ids=[document_id]
        )  #  idsとdocumentsの要素数を合わせる
        logging.info(f"Document added with UUID: {document_id}")
        return document_id

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
