from fastapi import FastAPI
from src.routers import chat
from src.routers import threads
from src.routers import rag
from src.middlewares.cors import add_cors_middleware

app = FastAPI()

add_cors_middleware(app)

app.include_router(chat.router)
app.include_router(threads.router)
app.include_router(rag.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
