#!/bin/bash

created=dev.db
export PYTHONPATH="${PYTHONPATH}:../"

if [ ! -f $created ]; then
    python manage.py migrate
    python manage.py createsuperuser
    # python manage.py loaddata data_fixtures.json
fi
# only for testing
python manage.py runserver 0.0.0.0:8000
