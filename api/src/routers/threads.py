from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from src.db import get_db
from src.usecases.chat_thread.read import read_chat_threads
from src.usecases.chat_thread.get_chat_messages_by_thread_id import get_chat_messages_by_thread_id

router = APIRouter(
    prefix="/threads",
    tags=["threads"],
)


@router.get("/")
async def get_threads(db: AsyncSession = Depends(get_db)):
    threads = await read_chat_threads(db)
    return threads

@router.get("/{thread_id}")
async def get_thread(thread_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    threads = await get_chat_messages_by_thread_id(db, thread_id)
    return threads