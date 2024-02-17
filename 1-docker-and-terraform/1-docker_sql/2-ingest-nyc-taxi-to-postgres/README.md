### Run a postgres container with CLI

```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DATABASE="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
 postgres:13
 ```

### Connect to pgcli using CLI to connect to this postgres container, it will prompt for password and enter password specified in above command to run postgres

```pgcli -h localhost -p 5432 -u root -d ny_taxi```

