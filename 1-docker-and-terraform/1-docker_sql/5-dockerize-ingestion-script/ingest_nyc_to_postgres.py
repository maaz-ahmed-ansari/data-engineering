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
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'
    
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

    # Since csv file has very huge data so getting it by iterator and in pandas it is made simple
    df_iterator = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iterator)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Create only on header so that DDL is executed without loading the data
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Now load the data
    df.to_sql(name=table_name, con=engine, if_exists='append')

    # Load rest of data by iterating
    while True:
        try:
            t_start = time()
            
            df = next(df_iterator)
            
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            
            df.to_sql(name=table_name, con=engine, if_exists='append')
            
            t_end = time()
            
            print(f'inserted another chunk {t_end - t_start}')

        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

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