from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from src.schemes.chat import ChatRequest
from src.usecases.chat_gpt.chat import chat_gpt
from src.usecases.chat_gpt.sse import stream_generate

router = APIRouter()


@router.get("/chat", tags=["chat"])
async def get_chat(request=Depends(ChatRequest)):
    """
    チャットを取得する
    """
    text = request.text
    message = chat_gpt(text)

    return {"chat": message}

@router.get("/chat/sse", tags=["chat"])
async def get_chat_sse(request=Depends(ChatRequest)):
    """
    SSEで回答する
    """
    text = request.text
    stream = stream_generate(text)

    return StreamingResponse(stream, media_type="text/plain")