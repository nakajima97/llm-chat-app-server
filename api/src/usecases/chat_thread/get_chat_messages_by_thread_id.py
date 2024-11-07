from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.chat_message import get_messages_by_thread_id

async def get_chat_messages_by_thread_id(db: AsyncSession, thread_id):
    return await get_messages_by_thread_id(db, thread_id)
