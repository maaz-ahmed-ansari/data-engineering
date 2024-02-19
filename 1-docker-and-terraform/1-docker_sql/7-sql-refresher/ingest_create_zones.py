#!/usr/bin/env python
import os
import pandas as pd
import argparse
from sqlalchemy import create_engine
from time import time


def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url

    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    if url.endswith('.csv.gz'):
        csv_name = 'zone_lookup.csv.gz'
    else:
        csv_name = 'zone_lookup.csv'
    
    csv_path = f"~/data-engineering/1-docker-and-terraform/1-docker_sql/{csv_name}"
    
    # Download CSV File
    os.system(f"wget {url} -O {csv_name}")

    # engine = create_engine("postgresql://scott:tiger@localhost/test")
    # scott -- user
    # tiger -- password
    # test -- DB name
    # you can specify port as well
    # create_engine("postgresql://scott:tiger@localhost:5432/test")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_csv(csv_name)

    df.to_sql(table_name, con = engine, if_exists = 'replace')

    print("Finished ingesting data into the postgres database")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='DB name for postgres')
    parser.add_argument('--table_name', help='name of the table in postgres')
    parser.add_argument('--url', help='url of the NYC CSV data')

    args = parser.parse_args()

    main(args)  