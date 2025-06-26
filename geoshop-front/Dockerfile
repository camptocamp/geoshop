# Build with node
FROM node:22.6.0-slim AS builder
LABEL org.opencontainers.image.authors="andrey.rusakov@camptocamp.com"
WORKDIR /geoshop-front

COPY config.json config.json
RUN apt update && apt install -y git && \
    git clone https://github.com/camptocamp/geoshop-front.git src && cd src && \
    cp /geoshop-front/config.json ./src/assets/configs/ && \
    npm ci --force && npm run build -- --localize

# Serve with nginx unpprevileged
FROM nginxinc/nginx-unprivileged:stable
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy build artifacts
COPY --from=builder /geoshop-front/src/dist/browser/de /usr/share/nginx/html/de
COPY --from=builder /geoshop-front/src/dist/browser/en /usr/share/nginx/html/en
COPY --from=builder /geoshop-front/src/dist/browser/fr /usr/share/nginx/html/fr
