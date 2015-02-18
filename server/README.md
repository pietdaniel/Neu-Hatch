# todo
- api requirements
- api specification
- models
- authentication
- authorization

# done
- basic oauth support
- search endpoint

# dependencies

- python2
- postgres
- http://tweepy.readthedocs.org/en/v3.2.0/index.html
- https://flask.pocoo.org/
- http://initd.org/psycopg/
- http://www.sqlalchemy.org/http://www.sqlalchemy.org/
- http://flask-migrate.readthedocs.org/en/latest/


# setup

### set up postgres

 - for mac users: http://postgresapp.com/
 - for arch users: https://wiki.archlinux.org/index.php/PostgreSQL

 after creating a postgres user, starting the daemon, and initializing the database

 create the database.
 ```
 postgres$ createdb neuhatch
 postgres$ psql -d neuhatch
 psql (9.4.0)
 Type "help" for help.

 neuhatch=#
 ```

### set up virtualenv

http://docs.python-guide.org/en/latest/dev/virtualenvs/ 

```
source /usr/bin/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python2 neuhatch
```

### install necessary dependencies

```
pip install -r requirements.txt
```

### export environment variables

in order to keep our keys secret, an environment variable file will need to be created.

Call this file ```ENVVAR``` and place it in ```server/```

Its format is as follows:

```
export CONSUMER_KEY="PLACEHOLDER"
export CONSUMER_SECRET="PLACEHOLDER"
export ACCESS_TOKEN="PLACEHOLDER"
export ACCESS_TOKEN_SECRET="PLACEHOLDER"
export APP_SECRET="PLACEHOLDER"
export HATCH_DB_USER="hatch"
export HATCH_DB_PASSWORD="whathaveyou"
export HATCH_DB_NAME="neuhatch"
export DATABASE_URI="postgres://${HATCH_DB_USER}:${HATCH_DB_PASSWORD}@db/${HATCH_DB_NAME}"
```

Then run:

```
source ENVVAR
```

###  initialize database and migrate the models

using ```manage.py``` initialize the database and migrate the models

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

you can verify the models exist in postgres like so:

```
psql -d neuhatch
neuhatch=# \dt
```

# run

```
./server/runserver.py
```



