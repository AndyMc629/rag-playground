#!/bin/bash

# Start the PostgreSQL service
#service postgresql start
postgres -D /var/lib/postgresql/data

# Optionally, run any database migrations or setup here

# Run your application (e.g., starting a Flask or Django server, etc.)
# Replace the following line with the command to start your application
#exec "$@"