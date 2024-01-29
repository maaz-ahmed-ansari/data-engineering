FROM python:3.10

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

# Directory in docker image
WORKDIR /app
# COPY source_on_host dest_on_docker
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]