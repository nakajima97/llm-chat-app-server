from sqlalchemy import Column, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from src.db import Base


class ChatThreads(Base):
    __tablename__ = "chat_threads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()
    )