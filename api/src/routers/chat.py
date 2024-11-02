from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemes.chat import ChatRequest
from src.usecases.chat_gpt.chat import chat_gpt
from src.usecases.chat_gpt.sse import stream_generate
from src.db import get_db
from src.repositories.chat_room import create_chat_room
from src.repositories.chat_history import create_chat_history

router = APIRouter()

@router.get("/chat", tags=["chat"])
async def get_chat(request=Depends(ChatRequest), db: AsyncSession = Depends(get_db)):
    """
    チャットを取得する
    """
    text = request.text
    chat_room_id = request.chat_room_id
    message = chat_gpt(text)

    if not chat_room_id:
        # Insert a new row into chat_room table
        new_chat_room = await create_chat_room(db)
        chat_room_id = new_chat_room.id

    # Insert into chat_histories table
    await create_chat_history(db, chat_room_id, text, 2)
    await create_chat_history(db, chat_room_id, message, 1)

    return {"chat": message}

@router.get("/chat/sse", tags=["chat"])
async def get_chat_sse(request=Depends(ChatRequest)):
    """
    SSEで回答する
    """
    text = request.text
    stream = stream_generate(text)

    return StreamingResponse(stream, media_type="text/plain")