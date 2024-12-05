#!/bin/bash
set -euo pipefail

psql --host=$PGHOST --username=$PGUSER --dbname=$PGDB  --set "geoshop_backend='$GEOSHOP_BACKEND'" \
  < /updatedb/001_update_db.sql  \
  < /updatedb/002_create_test_data.sql 
