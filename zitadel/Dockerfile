FROM golang:1.22-alpine AS builder
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"

COPY main.go /main.go
COPY client.go /client.go

RUN apk add git && \
    git clone https://github.com/camptocamp/zitadel-oidc /zitadel-oidc && \
    echo "replace github.com/zitadel/oidc => ." >> /zitadel-oidc/go.mod && \
    cp /main.go /zitadel-oidc/example/server/main.go && \
    cp /client.go /zitadel-oidc/example/server/storage/client.go && \
    cd /zitadel-oidc && go build github.com/zitadel/oidc/v3/example/server

FROM alpine:latest

ENV PORT=9998 \
    USERS_FILE=/zitadel/users.json \
    REDIRECT_URIS=http://frontend/geoshop/oidc/callback,http://frontend/geoshop/auth/oidc

RUN mkdir -p /zitadel/files
COPY --from=builder /zitadel-oidc/example/server/service-key1.json /zitadel-oidc/files/user_key.json
COPY --from=builder /zitadel-oidc/server /zitadel/server
COPY users.json /zitadel/users.json

ENTRYPOINT [ "/zitadel/server" ]