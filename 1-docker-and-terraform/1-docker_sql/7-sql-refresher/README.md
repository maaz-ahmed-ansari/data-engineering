# SQL Refresher

## Ingest zone_lookup data and create "zones" table

- Change directory to "6-postgres-and-pgddmin-with-docker-compose" and run ```docker-compose up```

- Then switch back to this directory "7-sql-refresher" and run below commands. (Note the network)

```
docker build -t zone_lookup:v1.2 .
```

```
URL="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"

docker run -it \
    --network=pg-network \
    zone_lookup:v1.2 \
        --user=root \
        --password=root \
        --host=pgdatabase \
        --port=5432 \
        --db=ny_taxi \
        --table_name=zones \
        --url=${URL}
```

## Connect to pgAdmin and analyze the data using SQL

- Some sample queries are written in sql-refresher.sql file