#!/bin/bash
set +e

podman pod create -n house-calendar-api -p 5432:5432 \
     -p 8000:8000 \
     -p 8080:8080 \
     -p 8443:8443 \
    --network=house-calendar-backend

podman run -dt --pod house-calendar-api \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=hc_events \
    -p 5432:5432 \
    --name=db \
    postgres:latest

podman run -dt --pod house-calendar-api \ 
    -e POSTGRES_MIGRATE_URL=postgresql+psycopg2://postgres:postgres@db:5432/hc_event \
    --name=api \
ghcr.io/howaboutudance/hematite/house-calendar-api

podman run -dt --pod house-calendar-api \
    --name pgadmin \
    bitnami/phppgadmin