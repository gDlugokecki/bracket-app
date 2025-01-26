include .env

build:
	docker compose build --no-cache
run:
	docker compose up
migrations:
	cd django_api && poetry run python manage.py makemigrations
run-migration:
	cd django_api && poetry run python manage.py makemigrations && cd .. && $(MAKE) build && $(MAKE) run