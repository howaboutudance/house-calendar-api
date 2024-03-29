#!/bin/bash
# Copyright 2021-2022 Michael Penhallegon 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

sleep 10

podman pod create \
    --network=${NETWORK_NAME} \
    -n alembic-init

podman run --pod alembic-init \
    -v ./config/:/app/config/:z \
    localhost/hematite/house-calendar-events-init