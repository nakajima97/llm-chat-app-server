from sqlalchemy.orm import Session
from src.models.chat_room import ChatRoom
from src.models.chat_room import ChatHistory

def create_chat_room(db: Session) -> ChatRoom:
    new_chat_room = ChatRoom()
    db.add(new_chat_room)
    db.commit()
    db.refresh(new_chat_room)
    return new_chat_room

def create_chat_history(db: Session, chat_room_id: int, message: str) -> ChatHistory:
    new_chat_history = ChatHistory(chat_room_id=chat_room_id, message=message)
    db.add(new_chat_history)
    db.commit()
    return new_chat_history
