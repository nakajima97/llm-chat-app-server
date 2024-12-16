import logging
from langchain_chroma import Chroma
from uuid import uuid4
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

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
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

        vector_store = Chroma(
            collection_name="example_collection",
            embedding_function=embeddings,
            persist_directory="./chroma_langchain_db",
        )

        # UUID を1つだけ生成して再利用
        document_id = str(uuid4())
        document = Document(
            page_content=content,
            metadata={"source": "save_chroma"},
            id=document_id,
        )

        vector_store.add_documents(documents=[document], ids=[document_id])  #  idsとdocumentsの要素数を合わせる
        logging.info(f"Document added with UUID: {document_id}")
        return document_id

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None