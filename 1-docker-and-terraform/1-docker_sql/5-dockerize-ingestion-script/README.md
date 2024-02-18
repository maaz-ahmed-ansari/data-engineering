# Putting the ingestion script into Docker

- Converting the Jupyter notebook to a Python script
- Parametrizing the script with argparse
- Dockerizing the ingestion script

## Run Python Script "Locally" to ingest

- Prerequisite: postgres must be running 

URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

python ingest_nyc_to_postgres.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL}


## Dockerize the ingestion script and run it in container network and connect and load data to postgres in network

- network must be specified in CLI 
    -because this docker will be isolated container and no postgres running on this, instead it is running on different container and it is in network
- "--host" is the name of the postgres instance/container which used while running inside network in last step i.e. '4-pgadmin-postgres' folder

- Run below command from [4-pgadmin-postgres](https://github.com/maaz-ahmed-ansari/data-engineering/tree/main/1-docker-and-terraform/1-docker_sql/4-pgadmin-postgres) folder

```
docker build -t taxi_ingest:v1.0 .
```

- Docker run

```
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

docker run -it \
    --network=pg-network \
    taxi_ingest:v1.0 \
        --user=root \
        --password=root \
        --host=pg-database-new \
        --port=5432 \
        --db=ny_taxi \
        --table_name=yellow_taxi_trips \
        --url=${URL}
```
