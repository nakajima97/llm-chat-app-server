from sqlalchemy.ext.asyncio import AsyncSession
from src.models.chat_room import ChatThreads


async def create_chat_room(db: AsyncSession) -> ChatThreads:
    new_chat_room = ChatThreads()
    db.add(new_chat_room)
    await db.commit()
    await db.refresh(new_chat_room)
    return new_chat_room
