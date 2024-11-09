import json
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemes.chat import ChatRequest, ChatResponse
from src.usecases.chat_thread.generate_thread import generate_thread
from src.usecases.chat_gpt.chat import chat_gpt
from src.usecases.chat_gpt.sse import stream_generator
from src.db import get_db
from src.usecases.chat_message.save import save_chat_message

router = APIRouter()


@router.get("/chat", tags=["chat"], response_model=ChatResponse)
async def get_chat(request=Depends(ChatRequest), db: AsyncSession = Depends(get_db)):
    """
    チャットを取得する
    """
    text = request.text
    chat_thread_id = request.chat_thread_id
    message = chat_gpt(text)

    # スレッドIDがない場合は新規作成
    if not chat_thread_id:
        chat_thread_id = await generate_thread(db, chat_thread_id, text)

    await save_chat_message(db, chat_thread_id, text, message)

    return {"data": {"thread_id": chat_thread_id, "content": message}}


@router.get("/chat/sse", tags=["chat"], response_model=ChatResponse)
async def get_chat_sse(
    request=Depends(ChatRequest), db: AsyncSession = Depends(get_db)
):
    """
    SSEで回答する
    """
    text = request.text
    chat_thread_id = request.chat_thread_id
    stream = stream_generator(text)

    # スレッドIDがない場合は新規作成
    if not chat_thread_id:
        chat_thread_id = await generate_thread(db, chat_thread_id, text)

    # DBにチャット履歴を保存するためにstreamをイベントジェネレータに変換
    async def event_generator():
        response = ""
        async for chunk in stream:
            response += chunk

            # SSE形式に変換
            data = json.dumps({"thread_id": str(chat_thread_id), "content": response})

            yield f"data: {data}\n\n"

        # streamが終了したらDBにチャット履歴を保存
        await save_chat_message(db, chat_thread_id, text, response)

    return StreamingResponse(event_generator(), media_type="text/plain")
