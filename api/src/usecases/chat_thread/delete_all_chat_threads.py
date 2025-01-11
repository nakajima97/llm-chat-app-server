from src.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.repositories.chat_thread import delete_all_chat_thread


async def delete_all_chat_threads(db: AsyncSession = Depends(get_db)):
    await delete_all_chat_thread(db)
