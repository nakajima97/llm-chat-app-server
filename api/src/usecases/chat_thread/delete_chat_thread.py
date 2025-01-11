import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.chat_thread import delete_chat_thread_by_id


async def delete_chat_thread(db: AsyncSession, thread_id: uuid.UUID) -> None:
    await delete_chat_thread_by_id(db, thread_id)