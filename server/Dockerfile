FROM debian:wheezy
MAINTAINER Isaac Boehman <idboehman@gmail.com>

RUN apt-get update && apt-get install -y \
    git \
    gunicorn \
    libmagic1 \
    libpq-dev \
    python2.7-dev \
    python-pip \
    python-software-properties \
    socat \
    software-properties-common \
    wget

# Add pgdg repo to installed postgresql versions > 9.1 in wheezy
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main' > /etc/apt/sources.list.d/pgdg.list
RUN wget -O - -q https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && apt-get install -y \
    postgresql-client-9.3 \
    postgresql-client-common \
    python-psycopg2

ADD requirements.txt /tmp/requirements.txt
RUN pip install virtualenv
# create virtualenv at /hatch_venv
RUN virtualenv hatch_venv
# Install requirements into virtualenv
RUN . /hatch_venv/bin/activate; pip install -r /tmp/requirements.txt
# Add script to run server from venv on container launch
ADD entrypoint.sh /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]