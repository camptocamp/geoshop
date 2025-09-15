FROM python:3.13-bookworm
LABEL org.opencontainers.image.authors="andrey.rusakov@camptocamp.com"

ENV  POETRY_NO_INTERACTION=1 \
     POETRY_VIRTUALENVS_CREATE=false \
     POETRY_CACHE_DIR='/var/cache/pypoetry' \
     POETRY_HOME='/usr/local' \
     OIDC_ENABLED=False

WORKDIR /app/geoshop_back
RUN apt update && apt install -y libgdal-dev libffi-dev gettext git && pip install poetry && \
    git clone https://github.com/camptocamp/geoshop-back .

RUN cp .env.sample .env && update-ca-certificates && python -m pip install truststore && \
    poetry install --only=main --no-root && \
    mv -vn default_settings.py settings.py && \
    sed -i 's/import sys/import sys\nimport truststore\ntruststore.inject_into_ssl()\n/g' manage.py && \
    sed -i 's/import os/import os\nimport truststore\ntruststore.inject_into_ssl()\n/g' settings.py && \
    sed -i 's/requests.get(discovery_url)/requests.get(discovery_url, verify=False)/g' settings.py && \
    sed -i 's/settings.OIDC_INTROSPECT_URL,/settings.OIDC_INTROSPECT_URL, verify=False,/g' oidc.py && \
    python manage.py collectstatic --noinput

# Compile locales
RUN python3 manage.py compilemessages
RUN rm -f .env

