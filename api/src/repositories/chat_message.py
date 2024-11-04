from sqlalchemy.ext.asyncio import AsyncSession
from src.models.chat_message import ChatMessage


async def create_chat_message(
    db: AsyncSession, chat_thread_id: int, message: str, role_id: int
) -> ChatMessage:
    new_chat_message = ChatMessage(
        chat_thread_id=chat_thread_id, message=message, role_id=role_id
    )
    db.add(new_chat_message)
    await db.commit()
    return new_chat_message
