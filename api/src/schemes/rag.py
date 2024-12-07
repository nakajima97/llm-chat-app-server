from pydantic import BaseModel, Field

class SavaTextRequest(BaseModel):
    title: str = Field(..., description="タイトル", example="テストデータ")
    content: str = Field(..., description="内容", example="これはテストデータです。")