#!/usr/bin/bash
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

if podman network exists ${NETWORK_NAME}; then
    podman pod kill postgres
    podman pod rm postgres -f
    podman pod kill alembic-init
    podman pod rm alembic-init -f
    podman network rm ${NETWORK_NAME}
else
    echo "${NETWORK_NAME} does not exists... exiting..."
fi