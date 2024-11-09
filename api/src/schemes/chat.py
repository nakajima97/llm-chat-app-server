from pydantic import BaseModel, Field

class ChatData(BaseModel):
    thread_id: str = Field(..., description="チャットルームID", example="123e4567-e89b-12d3-a456-426614174000")
    content: str = Field(..., description="チャット内容", example="こんにちは")

class ChatResponse(BaseModel):
    data: ChatData

class ChatRequest(BaseModel):
    text: str = Field(..., description="テキスト", example="こんにちは")
    chat_thread_id: str | None = Field(
        None,
        description="チャットルームID",
        example="123e4567-e89b-12d3-a456-426614174000",
    )
