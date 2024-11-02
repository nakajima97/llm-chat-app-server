from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    text: str = Field(..., description="テキスト", example="こんにちは")
    chat_room_id: str | None = Field(None, description="チャットルームID", example="123e4567-e89b-12d3-a456-426614174000")
