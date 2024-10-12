# fatapi-template
## Lint
`docker compose exec api poetry run ruff check`

## format
check  
`docker compose exec api poetry run ruff format --check`  
run  
`docker compose exec api poetry run ruff format`  

## migration
create migration file  
`docker compose exec api alembic revision --autogenerate -m "create initial table"`  

exec migration  
`docker compose exec api alembic upgrade head`  

init migration  
`docker compose exec api alembic downgrade base`  