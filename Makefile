start:
	docker-compose up -d

up:
	docker-compose up

down:
	docker-compose down

stop:
	docker-compose stop

build:
	docker-compose build

migrate:
	docker exec -it my_fastapi_project-web-1 alembic upgrade head

enter_db:
	docker exec -it my_fastapi_project-db-1 psql --username=fastapi_user --dbname=fastapi_db

reset: down start migrate stop up

