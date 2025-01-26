#!/bin/bash

# Run migrations
poetry run python manage.py migrate

# Start server
poetry run python manage.py runserver 0.0.0.0:8000