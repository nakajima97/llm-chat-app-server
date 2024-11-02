import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
CORS_ORIGIN = os.environ.get("CORS_ORIGIN")


def add_cors_middleware(app: FastAPI):
    # 許可するオリジンのリスト
    origins = CORS_ORIGIN.split(",")

    # CORSミドルウェアを追加
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # 許可するオリジン
        allow_credentials=True,
        allow_methods=["*"],  # 許可するHTTPメソッド
        allow_headers=["*"],  # 許可するHTTPヘッダー
    )
