from src.schemes.rag import SavaTextRequest
from fastapi import APIRouter, Depends

router = APIRouter(
  prefix="/rag",
  tags=["rag"]
)


@router.post("/")
async def save_text(request=Depends(SavaTextRequest)):
  return {"message": "Hello World"}