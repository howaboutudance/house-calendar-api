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

FROM ghcr.io/howaboutudance/hematite/python-base:3.10 as base
RUN dnf install python-devel gcc -y --nodocs --setopt install_weak_deps=False && \
    dnf clean all -y

FROM base as source
WORKDIR /app
COPY ./pyproject.toml ./ README.md ./ ./poetry.lock ./
RUN pip3 install poetry && poetry install --no-dev
COPY ./src/house_calendar_events/. ./src/house_calendar_events
COPY ./config/ ./

FROM source as builder
RUN set +x && poetry build -f wheel && ls /app/dist

FROM ghcr.io/howaboutudance/hematite/python-slim:3.10 as app
RUN microdnf install -y libpq-devel gcc python-devel \
     --nodocs --setopt install_weak_deps=0 && \
     pip install psycopg2
COPY --from=builder /app/dist/. /app/dist/
WORKDIR /app
RUN set +x && pip3 install dist/house_calendar_events*
ENV ENV_FOR_DYNACONF=ci
CMD python -m house_calendar_events

FROM ghcr.io/howaboutudance/hematite/python-slim as init
RUN microdnf install python3-alembic python3-psycopg2 -y --nodocs --setopt install_weak_deps=0 && \
    microdnf clean all -y
COPY --from=builder /app/dist/. /app/dist/
WORKDIR /app
RUN set +x && pip3 install dist/house_calendar_events*
COPY ./config/ ./
COPY ./alembic.ini .
COPY ./alembic/. ./alembic/
ENV ENV_FOR_DYNACONF=ci
ENTRYPOINT [ "alembic", "upgrade", "heads" ]