from sqlalchemy.future import select
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

async def get_messages_by_thread_id(db: AsyncSession, thread_id):
    # return db.query(ChatMessage).filter_by(thread_id=thread_id).order_by(ChatMessage.created_at.desc()).all()
    result = await db.execute(
        select(ChatMessage).filter(ChatMessage.chat_thread_id == thread_id).order_by(ChatMessage.created_at.desc())
    )
    return result.scalars().all()