FROM python:3.12-slim

RUN pip install poetry

WORKDIR /backend

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
ENV PATH="$PATH:$POETRY_HOME/bin"

ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=your_password

COPY ./django_api/pyproject.toml ./django_api/poetry.lock ./
COPY ./django_api/api/migrations ./migrations
COPY ./django_api/entrypoint.sh ./

RUN groupadd mygroup -g 1000
RUN useradd myuser -u 1000 -g 1000 -m -s /bin/bash

RUN poetry install

COPY ./django_api/manage.py ./
COPY ./django_api/api ./api
COPY ./django_api/core ./core

RUN chmod +x entrypoint.sh

# RUN poetry run python manage.py createsuperuser --noinput \
#     --username $DJANGO_SUPERUSER_USERNAME \
#     --email $DJANGO_SUPERUSER_EMAIL
# CMD ["poetry", "run", "python", "manage.py", "migrate", "&&", "runserver", "0.0.0.0:8000"]
CMD ["./entrypoint.sh"]
# CMD sleep infinity