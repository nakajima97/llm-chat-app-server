from sqlalchemy import Column, ForeignKey, Text, TIMESTAMP, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
from src.db import Base


class ChatHistory(Base):
    __tablename__ = 'chat_histories'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = Column(BigInteger, ForeignKey('roles.id'), nullable=False)
    chat_room_id = Column(UUID(as_uuid=True), ForeignKey('chat_rooms.id'), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    
    role = relationship('Role')
    chat_room = relationship('ChatRoom')
