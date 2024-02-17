FROM python:3.11

RUN pip install pandas

# Directory in docker image
WORKDIR /app

# COPY <source_on_host> <dest_on_docker>
COPY pipeline.py pipeline.py

ENTRYPOINT [ "python", "pipeline.py" ]