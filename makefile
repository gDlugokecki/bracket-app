include .env

build-clean:
	 docker compose build --no-cache
build:
	docker compose build
down:
	docker compose down
run:
	docker compose up --build --watch
migrations:
	docker compose run backend poetry run python manage.py makemigrations
run-migrate:
	docker compose run backend poetry run python manage.py migrate
root-shell:
	docker compose run --user 0 backend /bin/bash
populate-data:
	docker compose run backend poetry run python manage.py create_sample_data
api-migrations:
	docker compose exec api poetry run alembic revision --autogenerate -m "$(msg)"
api-migrate:
	docker compose exec api poetry run alembic upgrade head