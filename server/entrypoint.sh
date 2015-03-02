#!/bin/sh

. /hatch_venv/bin/activate

# Perform initial migrations if needed
if [ ! -d "migrations/" ]; then
  python manage.py db init
  python manage.py db migrate
fi

python manage.py db upgrade
python runserver.py -h 0.0.0.0 -p 5000
