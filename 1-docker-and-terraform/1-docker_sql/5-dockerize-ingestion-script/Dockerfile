FROM python:3.11

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2-binary

WORKDIR /app

COPY ingest_nyc_to_postgres.py ingest_nyc_to_postgres.py

ENTRYPOINT [ "python", "ingest_nyc_to_postgres.py" ]