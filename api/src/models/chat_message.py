from sqlalchemy import Column, ForeignKey, Text, TIMESTAMP, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from src.databases.relational.postgresql import Base

# これがないとRoleが見つからないとエラーが出る
from src.models.role import Role  # noqa


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = Column(BigInteger, ForeignKey("roles.id"), nullable=False)
    chat_thread_id = Column(
        UUID(as_uuid=True), ForeignKey("chat_threads.id"), nullable=False
    )
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()
    )

    role = relationship("Role")
    chat_thread = relationship("ChatThreads")
