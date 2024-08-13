#!/bin/bash
set -euo pipefail

cd /geoshop/geoshop-back

if [[ "$( python3 manage.py showmigrations | grep '\[ \]' )" != "" ]]; then
    python3 manage.py migrate --noinput
else
    echo "No pending migrations"
fi

if [[ ! -f "/geoshop/.fixtures_lock" ]]; then
    python3 manage.py fixturize
    if [[ $? == 0 ]]; then 
      touch "/geoshop/.fixtures_lock" 
    fi
else
    echo "No fixturizing needed."
fi

python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
