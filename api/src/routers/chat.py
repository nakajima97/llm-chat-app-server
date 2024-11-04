from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemes.chat import ChatRequest
from src.usecases.chat_gpt.chat import chat_gpt
from src.usecases.chat_gpt.sse import stream_generator
from src.db import get_db
from src.usecases.chat_history.save import save_chat_history

router = APIRouter()


@router.get("/chat", tags=["chat"])
async def get_chat(request=Depends(ChatRequest), db: AsyncSession = Depends(get_db)):
    """
    チャットを取得する
    """
    text = request.text
    chat_room_id = request.chat_room_id
    message = chat_gpt(text)

    await save_chat_history(db, chat_room_id, text, message)

    return {"chat": message}


@router.get("/chat/sse", tags=["chat"])
async def get_chat_sse(request=Depends(ChatRequest), db: AsyncSession = Depends(get_db)):
    """
    SSEで回答する
    """
    text = request.text
    chat_room_id = request.chat_room_id
    stream = stream_generator(text)

    # DBにチャット履歴を保存するためにstreamをイベントジェネレータに変換
    async def event_generator():
        response = ""
        async for chunk in stream:
            response += chunk
            yield chunk
        # streamが終了したらDBにチャット履歴を保存
        await save_chat_history(db, chat_room_id, text, response)

    return StreamingResponse(event_generator(), media_type="text/plain")
