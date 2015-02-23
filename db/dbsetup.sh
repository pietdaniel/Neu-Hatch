gosu postgres postgres --single -jE <<-EOSQL
  CREATE ROLE ${HATCH_DB_USER} WITH CREATEDB LOGIN ;
EOSQL

gosu postgres postgres --single -jE <<-EOSQL
  CREATE DATABASE ${HATCH_DB_NAME} OWNER ${HATCH_DB_USER} ;
EOSQL

# add pg_hba entry for docker network
{ echo; echo "host all all 172.17.0.0/24 trust"; } >> "${PGDATA}"/pg_hba.conf
