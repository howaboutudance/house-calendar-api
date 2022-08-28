#!/bin/bash

set +x

NETWORK_NAME=house-calendar-events

if podman network exists ${NETWORK_NAME}; then
    podman pod kill app
    podman pod rm app
    source ./scripts/podman-dn.sh
    source ./scripts/podman-up.sh
else
    source ./scripts/podman-up.sh
fi

podman pod create \
    --network=${NETWORK_NAME} \
    -n app \
    -p 8000:8000

podman run -dt --pod app \
    -v ./config:/config \
    localhost/hematite/house-calendar-events