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

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz```

```jupyter notebook```

To decompress .gz files, use:

```gzip -d filename.gz```

Take sample of csv file

```head -n 100 yellow_tripdata_2021-01.csv > yellow_head.csv```

Since original file has much larger records

```wc -l yellow_tripdata_2021-01.csv``` output >>>  1369766 yellow_tripdata_2021-01.csv


### Ingest data using python script using iteration over csv file

- code is written in ```ingest_nyc_to_postgres.ipynb``` along with comments

