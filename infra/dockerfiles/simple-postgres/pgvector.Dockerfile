# Dockerfile
FROM postgres:latest

RUN apt-get update && \
    apt-get install -y git postgresql-server-dev-all gcc make && \
    git clone https://github.com/pgvector/pgvector.git && \
    cd pgvector && \
    make && \
    make install && \
    apt-get remove -y gcc make postgresql-server-dev-all && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /pgvector