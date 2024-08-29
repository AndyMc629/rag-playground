# Use the base Python DevContainer image
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1

# Install PostgreSQL and necessary dependencies for pgvector
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
       postgresql \
       postgresql-contrib \
       postgresql-server-dev-all \
       build-essential \
       git \
    && rm -rf /var/lib/apt/lists/*

# Install pgvector
RUN git clone https://github.com/pgvector/pgvector.git /tmp/pgvector \
    && cd /tmp/pgvector \
    && make \
    && make install \
    && rm -rf /tmp/pgvector

# Set up the PostgreSQL data directory and configuration
RUN service postgresql start \
    && su postgres -c "psql -c \"CREATE EXTENSION IF NOT EXISTS vector;\"" \
    && su postgres -c "psql -c \"CREATE DATABASE vectorexample;\"" \
    && su postgres -c "psql -c \"ALTER USER postgres WITH PASSWORD 'postgres';\""

# Copy application requirements and install them
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Add the script to start PostgreSQL and your app
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Default command to run when starting the container
#CMD ["start.sh"]
# Ensure PostgreSQL runs in the foreground
CMD ["postgres", "-D", "/var/lib/postgresql/data"]

# FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# ENV PYTHONUNBUFFERED 1

# # [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# # [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends postgresql-client



