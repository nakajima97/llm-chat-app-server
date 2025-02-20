from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.configs.env import Env


def add_cors_middleware(app: FastAPI):
    # 許可するオリジンのリスト
    origins = Env.CORS_ORIGIN.split(",")

    # CORSミドルウェアを追加
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # 許可するオリジン
        allow_credentials=True,
        allow_methods=["*"],  # 許可するHTTPメソッド
        allow_headers=["*"],  # 許可するHTTPヘッダー
    )
