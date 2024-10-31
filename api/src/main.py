from fastapi import FastAPI
from src.routers import chat
from src.middleware import add_cors_middleware

app = FastAPI()

add_cors_middleware(app)

app.include_router(chat.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
