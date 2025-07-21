FROM python:alpine

RUN apk update --no-cache && \
    pip install --no-cache-dir selenium

ENTRYPOINT [ "bash", "-c", "python", "/tests/*.py" ]

