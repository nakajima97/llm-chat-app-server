from src.schemes.rag import SavaTextRequest, SavaTextResponse
from fastapi import APIRouter, Depends

router = APIRouter(
  prefix="/rag",
  tags=["rag"]
)


@router.post("/", response_model=SavaTextResponse)
async def save_text(request=Depends(SavaTextRequest)):
  return {"message": "Hello World"}