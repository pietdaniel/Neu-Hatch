FROM postgres:9.4
MAINTAINER Isaac Boehman <idboehman@gmail.com>

#ENV POSTGRES_PASSWORD wowmuchsecuresolocked

RUN [ -d "/docker-entrypoint-initdb.d" ] || mkdir /docker-entrypoint-initdb.d

COPY dbsetup.sh /docker-entrypoint-initdb.d/
