from fastapi import APIRouter, Depends
from src.usecases.vector_store.save_vector_store import save_vector_store
from src.schemes.rag import SavaTextRequest, SavaTextResponse

router = APIRouter(
  prefix="/rag",
  tags=["rag"]
)


@router.post("/", response_model=SavaTextResponse)
async def save_text(request: SavaTextRequest):
  save_vector_store(request.content)
  return {"result": "success"}