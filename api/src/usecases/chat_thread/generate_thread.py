from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.chat_thread import create_chat_thread
from src.usecases.chat_thread.generate_title import generate_title


async def generate_thread(
    db: AsyncSession, chat_thread_id: int | None, text: str
) -> None:
    """
    チャット履歴を保存する
    """
    title = generate_title(text)
    new_chat_thread = await create_chat_thread(db, title)
    chat_thread_id = new_chat_thread.id

    return chat_thread_id
