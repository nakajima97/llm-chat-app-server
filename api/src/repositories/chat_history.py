from sqlalchemy.ext.asyncio import AsyncSession
from src.models.chat_history import ChatHistory

async def create_chat_history(db: AsyncSession, chat_room_id: int, message: str, role_id: int) -> ChatHistory:
    new_chat_history = ChatHistory(chat_room_id=chat_room_id, message=message, role_id=role_id)
    db.add(new_chat_history)
    await db.commit()
    return new_chat_history