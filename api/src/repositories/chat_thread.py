from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.chat_thread import ChatThreads


async def create_chat_thread(db: AsyncSession) -> ChatThreads:
    new_chat_thread = ChatThreads()
    db.add(new_chat_thread)
    await db.commit()
    await db.refresh(new_chat_thread)
    return new_chat_thread


async def get_chat_threads(db: AsyncSession) -> list[ChatThreads]:
    result = await db.execute(select(ChatThreads))
    return result.scalars().all()
