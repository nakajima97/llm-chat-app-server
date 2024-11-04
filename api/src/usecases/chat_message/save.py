from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.chat_thread import create_chat_thread
from src.repositories.chat_message import create_chat_message
from src.constants import ChatRoleId


async def save_chat_message(
    db: AsyncSession, chat_thread_id: int | None, text: str, message: str
) -> None:
    """
    チャット履歴を保存する
    """
    if not chat_thread_id:
        # Insert a new row into chat_thread table
        new_chat_thread = await create_chat_thread(db)
        chat_thread_id = new_chat_thread.id

    # ユーザの質問を保存
    await create_chat_message(db, chat_thread_id, text, ChatRoleId.USER)

    # LLMの回答を保存
    await create_chat_message(db, chat_thread_id, message, ChatRoleId.ASSISTANT)

    return
