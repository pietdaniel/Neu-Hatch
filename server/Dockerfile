FROM ubuntu:14.04
MAINTAINER Isaac Boehman <idboehman@gmail.com>

RUN apt-get update && apt-get install -y \
    git \
    gunicorn \
    libmagic1 \
    libpq-dev \
    postgresql-client-9.3 \
    postgresql-client-common \
    python2.7-dev \
    python-pip \
    python-psycopg2 \
    python-software-properties \
    socat \
    software-properties-common

RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

EXPOSE 5000
