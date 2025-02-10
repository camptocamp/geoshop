FROM python:3.12.5-slim-bookworm
LABEL org.opencontainers.image.authors="andrey.rusakov@camptocamp.com"

ENV  POETRY_NO_INTERACTION=1 \
     POETRY_VIRTUALENVS_CREATE=false \
     POETRY_CACHE_DIR='/var/cache/pypoetry' \
     POETRY_HOME='/usr/local'

WORKDIR /app/geoshop_back
COPY geoshop-back.env .env
RUN apt update && apt install -y libgdal-dev libffi-dev gettext git && \
    pip install poetry && \
    git clone https://github.com/camptocamp/geoshop-back src && cp -rf src/* ./ && rm -rf src && \
    poetry install --only=main --no-root && mv -vn default_settings.py settings.py && \
    python manage.py collectstatic --noinput
EXPOSE 8000

