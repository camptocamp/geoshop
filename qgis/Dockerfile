FROM nginx:1.25.3

LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html
COPY .htpasswd /etc/nginx