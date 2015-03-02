#!/bin/sh

. /hatch_venv/bin/activate
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python runserver.py -h 0.0.0.0 -p 5000
