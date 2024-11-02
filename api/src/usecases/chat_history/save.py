from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.chat_room import create_chat_room
from src.repositories.chat_history import create_chat_history


async def save_chat_history(
    db: AsyncSession, chat_room_id: int | None, text: str, message: str
) -> None:
    """
    チャット履歴を保存する
    """
    if not chat_room_id:
        # Insert a new row into chat_room table
        new_chat_room = await create_chat_room(db)
        chat_room_id = new_chat_room.id

    # ユーザの質問を保存
    await create_chat_history(db, chat_room_id, text, 2)

    # LLMの回答を保存
    await create_chat_history(db, chat_room_id, message, 1)

    return
