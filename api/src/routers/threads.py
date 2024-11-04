from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_db
from src.usecases.chat_thread.read import read_chat_threads

router = APIRouter(
    prefix="/threads",
    tags=["threads"],
)


@router.get("/")
async def get_threads(db: AsyncSession = Depends(get_db)):
    threads = await read_chat_threads(db)
    return threads
