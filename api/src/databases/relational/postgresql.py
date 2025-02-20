from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from src.configs.env import Env

DB_URL = f"postgresql+asyncpg://{Env.DB_USER}:{Env.DB_PASSWORD}@{Env.DB_HOST}:{Env.DB_PORT}/{Env.DB_NAME}"

db_engine = create_async_engine(DB_URL, echo=True)
db_session = sessionmaker(
    bind=db_engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


async def get_db():
    async with db_session() as session:
        yield session
