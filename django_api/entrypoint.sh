#!/bin/bash

# create superuser
poetry run python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL || true

# Run migrations
poetry run python manage.py migrate

# Start server
poetry run python manage.py runserver 0.0.0.0:8000
