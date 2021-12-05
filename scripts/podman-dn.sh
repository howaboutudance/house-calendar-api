#!/usr/bin/bash

set +e

podman pod rm api_pod -f
podman pod rm phppgadmin_pod -f
podman pod rm db -f