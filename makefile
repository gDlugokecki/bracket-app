include .env

build-clean:
	 docker compose build --no-cache
build:
	docker compose build
run:
	docker compose up
migrations:
	docker compose run backend poetry run python manage.py makemigrations
run-migrate:
	docker compose run backend poetry run python manage.py migrate
root-shell:
	docker compose run --user 0 backend /bin/bash
populate-data:
	docker compose run backend poetry run python manage.py create_sample_data
