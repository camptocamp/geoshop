FROM python:3.12.5-slim-bookworm
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"
WORKDIR /geoshop/

ENV  POETRY_NO_INTERACTION=1 \
     POETRY_VIRTUALENVS_CREATE=false \
     POETRY_CACHE_DIR='/var/cache/pypoetry' \
     POETRY_HOME='/usr/local'

RUN apt update && \
    apt install -y git libgdal-dev libffi-dev gettext && \
    pip install poetry && \
    git clone https://github.com/camptocamp/geoshop-back.git /geoshop/geoshop-back && \
    cd /geoshop/geoshop-back && \
    poetry install --only=main

COPY settings.py /geoshop/geoshop-back/settings.py

COPY entrypoint.sh /geoshop/entrypoint.sh

ENTRYPOINT [ "/geoshop/entrypoint.sh" ]
