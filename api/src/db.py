from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "postgresql+asyncpg://user:password@postgres:5432/mydb"

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