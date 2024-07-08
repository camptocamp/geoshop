# Update the schema
FROM postgres:12-alpine
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"

# Addition packages
RUN apk update && \
    apk upgrade && \
    apk add curl git && \
    git clone https://github.com/asit-asso/extract /extract && \
    rm -rfv /var/cache/apk/* && \
    cp /extract/docker/update-db/update-db-when-ready.sh / && \
    cp /extract/sql/create_test_data.sql / && \
    cp /extract/sql/update_db.sql /

# Apply the changes
CMD cd / && \
    psql --host=$PGHOST --username=$PGUSER --dbname=$PGDB < /update_db.sql && \
    psql --host=$PGHOST --username=$PGUSER --dbname=$PGDB < /create_test_data.sql

# No entry point, exit gracefully
ENTRYPOINT []