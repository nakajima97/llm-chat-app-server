import json
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from langchain.schema import HumanMessage

from src.schemes.chat import ChatRequest, ChatResponse
from src.usecases.chat_thread.generate_thread import generate_thread
from src.usecases.chat_gpt.generate_chat_response import generate_chat_response
from src.usecases.chat_gpt.streaming_chat_responses import streaming_chat_responses
from src.db import get_db
from src.usecases.chat_message.save_chat_message import save_chat_message
from src.usecases.chat_gpt.fetch_and_format_chat_messages import (
    fetch_and_format_chat_messages,
)

router = APIRouter()


@router.get("/chat", tags=["chat"], response_model=ChatResponse)
async def get_chat(request=Depends(ChatRequest), db: AsyncSession = Depends(get_db)):
    """
    チャットを取得する
    """
    text = request.text
    chat_thread_id = request.chat_thread_id
    message = generate_chat_response(text)

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
    chat_thread_id = request.thread_id

    # DBから過去のやり取りを取得する
    formatted_messages = await fetch_and_format_chat_messages(db, chat_thread_id)

    # GETリクエストで送られてきたtextをHumanMessageに変換して追加
    formatted_messages.append(HumanMessage(content=text))

    # 回答のstreamを生成する
    stream = streaming_chat_responses(formatted_messages)

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
