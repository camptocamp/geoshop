FROM python:alpine

RUN apk update --no-cache && apk add firefox geckodriver && \
    pip install --no-cache-dir selenium selenium-firefox

WORKDIR /tests
ENTRYPOINT [ "python", "-m", "unittest", "discover", "--pattern=*.py" ]
