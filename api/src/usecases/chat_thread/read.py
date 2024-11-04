from sqlalchemy.ext.asyncio import AsyncSession
from src.models.chat_thread import ChatThreads
from src.repositories.chat_thread import get_chat_threads

async def read_chat_threads(db: AsyncSession) -> list[ChatThreads]:
    '''
    スレッドの一覧を取得する
    '''
    return await get_chat_threads(db)