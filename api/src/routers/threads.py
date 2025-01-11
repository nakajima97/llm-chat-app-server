from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from src.db import get_db
from src.usecases.chat_thread.read_chat_threads import read_chat_threads
from src.usecases.chat_thread.get_chat_messages_by_thread_id import (
    get_chat_messages_by_thread_id,
)
from src.usecases.chat_thread.delete_chat_thread import delete_chat_thread
from src.usecases.chat_thread.delete_all_chat_threads import delete_all_chat_threads

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


@router.delete("/{thread_id}")
async def delete_thread(thread_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    await delete_chat_thread(db, thread_id)
    return {"message": "Thread deleted successfully"}


@router.delete("/")
async def delete_all_thread(db: AsyncSession = Depends(get_db)):
    await delete_all_chat_threads(db)
    return {"message": "All threads deleted successfully"}
