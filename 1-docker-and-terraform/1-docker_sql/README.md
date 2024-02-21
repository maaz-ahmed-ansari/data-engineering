# Containerization

- Docker and docker-compose
- Running Postgres locally with Docker

## Introduction to Docker 

[Instructions](1-docker-basics)

- Why do we need Docker
- Creating a simple "data pipeline" in Docker

## Ingesting NY Taxi Data to Postgres

[Instructions](2-ingest-nyc-taxi-to-postgres)

- Running Postgres locally with Docker
- Using pgcli for connecting to the database
- Exploring the NY Taxi dataset
- Ingesting the data into the database

## Connect jupyter notebook using pandas to postgres running in a container

[Instructions](3-connect-jupyter-to-postgres)

## Connecting pgAdmin and Postgres

[Instructions](4-pgadmin-postgres)

- The pgAdmin tool
- Docker networks

## Putting the ingestion script into Docker

[Instructions](5-dockerize-ingestion-script)

- Converting the Jupyter notebook to a Python script
- Parametrizing the script with argparse
- Dockerizing the ingestion script

## Running Postgres and pgAdmin with Docker-Compose

[Instructions](6-postgres-and-pgddmin-with-docker-compose)

- Why do we need Docker-compose
- Docker-compose YAML file
- Running multiple containers with docker-compose up

## SQL refresher

[Instructions](7-sql-refresher)

- Adding the Zones table
- Inner joins
- Basic data quality checks
- Left, Right and Outer joins
- Group by