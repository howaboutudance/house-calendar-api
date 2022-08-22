#!/bin/bash
set +e

NETWORK_NAME=house-calendar-events

podman network create ${NETWORK_NAME}

podman pod create \
  --network=${NETWORK_NAME} \
  -n postgres \
  -p 5432:5432 \

podman run -dt --pod postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=hc_events \
  docker.io/postgres