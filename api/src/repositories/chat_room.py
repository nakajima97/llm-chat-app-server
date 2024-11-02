from sqlalchemy.ext.asyncio import AsyncSession
from src.models.chat_room import ChatRoom


async def create_chat_room(db: AsyncSession) -> ChatRoom:
    new_chat_room = ChatRoom()
    db.add(new_chat_room)
    await db.commit()
    await db.refresh(new_chat_room)
    return new_chat_room
