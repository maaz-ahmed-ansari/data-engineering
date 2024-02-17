#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import argparse

from time import time
from sqlalchemy import create_engine

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

    # Download csv file
    os.system(f"wget {url} -O {csv_name}")

    # Create engine/connection
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Create iterator reading chunksize=100000 i.e. 100000 lines from csv file
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # next(iterator) to get next iterator
    df = next(df_iter)

    # Type conversion
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Create table only without inserting any data yet
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')
    
    # Now insert all data going through iterator
    # When there is no data in iterator, it'll through exception and the infinite loop will exit
    while True:

        try:
            t_start = time()
            df = next(df_iter)
            
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            
            df.to_sql(name=table_name, con=engine, if_exists='append')
            
            t_end = time()

            print('Inserted another chunk..., took %.3f seconds' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import CSV data to Postgres')
    # user, password, host, port, database name, table name,
    # url of the csv 
    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)

