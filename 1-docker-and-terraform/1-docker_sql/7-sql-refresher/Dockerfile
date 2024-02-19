FROM python:3.11

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2-binary

WORKDIR /app

COPY ingest_create_zones.py ingest_create_zones.py

ENTRYPOINT [ "python", "ingest_create_zones.py" ]