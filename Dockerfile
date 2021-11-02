# Copyright 2021 Michael Penhallegon 
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

FROM python:3.9 as source 
WORKDIR /app
COPY ./requirements.txt ./
COPY ./setup.py ./ README.md ./
RUN pip3 install -r requirements.txt
COPY ./house_calendar/. ./house_calendar

FROM source as test
COPY ./test ./test
COPY ./tox.ini ./ ./requirements-dev.txt ./
RUN pip3 install -r requirements-dev.txt
CMD tox -e py38 && mypy house_calendar/

FROM source as builder
RUN pip3 install wheel
RUN python setup.py bdist_wheel

FROM python:3.9-slim as app
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
COPY --from=builder /app/dist ./app/dist
WORKDIR /app
RUN pip3 install dist/house_calendar*
ENV HOST_SERVER 0.0.0.0
ENV POSTGRES_MIGRATE_URI postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/hc_events
COPY ./alembic.ini .
COPY ./alembic/. ./alembic/
CMD alembic upgrade heads && python -m house_calendar