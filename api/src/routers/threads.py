from fastapi import APIRouter

router = APIRouter(
    prefix="/threads",
    tags=["threads"],
)


@router.get("/")
async def get_threads():
    return {"threads": "threads"}
