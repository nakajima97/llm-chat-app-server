import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.sql import func

from src.models.chat_thread import ChatThreads


async def create_chat_thread(db: AsyncSession, title: str) -> ChatThreads:
    new_chat_thread = ChatThreads(title=title)
    db.add(new_chat_thread)
    await db.commit()
    await db.refresh(new_chat_thread)
    return new_chat_thread


async def get_chat_threads(db: AsyncSession) -> list[ChatThreads]:
    result = await db.execute(
        select(ChatThreads).where(ChatThreads.deleted_at.is_(None))
    )
    return result.scalars().all()


async def delete_chat_thread_by_id(db: AsyncSession, thread_id: uuid.UUID) -> None:
    stmt = (
        update(ChatThreads)
        .where(ChatThreads.id == thread_id)
        .values(deleted_at=func.now())
    )
    await db.execute(stmt)
    await db.commit()
