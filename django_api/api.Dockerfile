FROM python:3.12-slim

RUN groupadd mygroup -g 1000 && \
    useradd myuser -u 1000 -g 1000 -m -s /bin/bash

RUN mkdir /opt/poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_HOME=/opt/poetry

ENV PATH="$POETRY_HOME/bin:${PATH}"

RUN apt -y update && apt -y install curl
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.5 python3 -

WORKDIR /backend



COPY --chown=myuser:mygroup ./django_api/pyproject.toml ./django_api/poetry.lock ./
COPY --chown=myuser:mygroup ./django_api/entrypoint.sh ./

# Install dependencies as root (required for system-level installations)
RUN poetry install
RUN rm -rf $POETRY_CACHE_DIR

# Set ownership of the working directory
RUN chown myuser:mygroup /backend

# Copy application files with correct ownership
COPY --chown=myuser:mygroup ./django_api/manage.py ./
COPY --chown=myuser:mygroup ./django_api/apps ./apps
COPY --chown=myuser:mygroup ./django_api/core ./core

# # Ensure entrypoint is executable
RUN chmod +x entrypoint.sh

# # Switch to non-root user
USER myuser

CMD ["./entrypoint.sh"]
# CMD sleep infinity
