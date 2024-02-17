FROM python:3.11

RUN pip install pandas

# RUN apt-get install wget
# RUN pip install pandas sqlalchemy psycopg2

# # Directory in docker image
WORKDIR /app
# # COPY source_on_host dest_on_docker
COPY pipeline.py pipeline.py
# COPY ingest_data.py ingest_data.py/   0000000000000000.333

# ENTRYPOINT [ "python", "ingest_data.py" ]

ENTRYPOINT [ "python", "pipeline.py" ]