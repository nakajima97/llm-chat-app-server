from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/chat", tags=["chat"])
async def get_chat():
    ```
    Chat GPTとのチャットを行う
    ```
    return {"chat": "chat"}