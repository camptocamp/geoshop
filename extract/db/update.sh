#!/bin/bash
set -euo pipefail

psql --host=$POSTGRES_HOST --username=$POSTGRES_USER --dbname=$POSTGRES_DB --set "geoshop_backend='$GEOSHOP_BACKEND'" \
  < /updatedb/001_updatedb.sql  \
  < /updatedb/002_testconfig.sql
