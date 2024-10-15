FROM golang:1.22-alpine AS builder
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"

RUN apk add git && \
    git clone https://github.com/camptocamp/zitadel-oidc /zitadel-oidc && \
    echo "replace github.com/zitadel/oidc => ." >> /zitadel-oidc/go.mod && \
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