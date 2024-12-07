from pydantic import BaseModel, Field

class SavaTextRequest(BaseModel):
    title: str = Field(..., description="タイトル", example="テストデータ")
    content: str = Field(..., description="内容", example="これはテストデータです。")

class SavaTextResponse(BaseModel):
    result: str = Field(..., description="結果", example="success")