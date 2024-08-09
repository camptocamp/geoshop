FROM python:3.12.5-slim-bookworm
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"
WORKDIR /geoshop/

ENV  POETRY_NO_INTERACTION=1 \
     POETRY_VIRTUALENVS_CREATE=false \
     POETRY_CACHE_DIR='/var/cache/pypoetry' \
     POETRY_HOME='/usr/local'

RUN apt update && \
    apt install -y git curl libgdal-dev libffi-dev postgresql && \
    pip install poetry && \
    git clone https://github.com/camptocamp/geoshop-back.git /geoshop/geoshop-back && \
    cd /geoshop/geoshop-back && \
    poetry install --only=main

# FIXME: Add this through the containder od the composition
COPY .env /geoshop/geoshop-back/.env
COPY settings.py /geoshop/geoshop-back/settings.py
COPY resource/sampledata.sql /geoshop/sampledata.sql
COPY entrypoint.sh /geoshop/entrypoint.sh

# Copy default settings to settings only if there is no such file
RUN mv -vn /geoshop/geoshop-back/default_settings.py /geoshop/geoshop-back/settings.py
ENTRYPOINT [ "/geoshop/entrypoint.sh" ]
