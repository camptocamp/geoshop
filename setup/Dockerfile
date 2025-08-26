FROM python:alpine

RUN apk update --no-cache && apk add firefox geckodriver openssl && \
    pip install --no-cache-dir selenium selenium-firefox

WORKDIR /setup
