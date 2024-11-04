# fatapi-template
## 概要
LLMとチャットができるアプリ  
フロントは以下リポジトリ  
https://github.com/nakajima97/llm-chat-app-front
## Setup
`docker compose up`

## Lint
`docker compose exec api uv run ruff check`

## format
check  
`docker compose exec api uv run ruff format --check`  
run  
`docker compose exec api uv run ruff format`  

## migration
create migration file  
`docker compose exec api uv run alembic revision --autogenerate -m "create initial table"`  

exec migration  
`docker compose exec api uv run alembic upgrade head`  

init migration  
`docker compose exec api uv run alembic downgrade base`  

## seeder
`docker compose exec api uv run -m src.seeders.role`

## test sse with curl
`curl -N -H "Accept: text/event-stream" "http://localhost:8000/chat/sse?text=%E3%83%86%E3%82%B9%E3%83%88"`