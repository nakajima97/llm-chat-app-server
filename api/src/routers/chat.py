from fastapi import APIRouter, Depends

from src.schemes.chat import ChatRequest
from src.usecases.chat_gpt.chat import chat_gpt

router = APIRouter()

@router.get("/chat", tags=["chat"])
async def get_chat(request=Depends(ChatRequest)):
    '''
    チャットを取得する
    '''
    text = request.text
    message = chat_gpt(text)

    return {"chat": message}