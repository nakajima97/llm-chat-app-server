from sqlalchemy.ext.asyncio import AsyncSession
from langchain.schema import HumanMessage, AIMessage

from src.repositories.chat_message import get_messages_by_thread_id
from src.configs.constants import ChatRoleId


async def fetch_and_format_chat_messages(db: AsyncSession, thread_id: str):
    """
    スレッドIDをもとにDBからチャット一覧を取得してLangChainで使える形に変換する
    """
    # チャット履歴を取得
    messages = await get_messages_by_thread_id(db, thread_id)

    # LangChainのHumanMessage、AIMessageに変換
    formatted_messages = []
    for message in messages:
        if message.role_id == ChatRoleId.USER:
            formatted_messages.append(HumanMessage(content=message.message))
        elif message.role_id == ChatRoleId.ASSISTANT:
            formatted_messages.append(AIMessage(content=message.message))

    return formatted_messages
