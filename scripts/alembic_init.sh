#!/bin/bash

# Funtional test of alembic upgrade container to test adding checks of roll-out

set +x

NETWORK_NAME=house-calendar-events

podman network create ${NETWORK_NAME}

podman pod create \
    --network=${NETWORK_NAME} \
    -n postgres \
    -p 5432:5432

podman run -dt --pod postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=hc_events \
    docker.io/postgres

podman pod create \
    --network=${NETWORK_NAME} \
    -n alembic-init

podman run --pod alembic-init \
    -v ./config/:/app/config/:z \
    localhost/hematite/house-calendar-events-init