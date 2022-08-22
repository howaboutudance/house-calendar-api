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

BASE_TAG = hematite/house-calendar
TEST_TAG = ${BASE_TAG}-test
APP_TAG = ${BASE_TAG}-api
INIT_TAG = ${BASE_TAG}-init
CR_REGISTRY = ghcr.io/howaboutudance
APP_REPO_TAG =  ${CR_REGISTRY}/${APP_TAG}
INIT_REPO_TAG = ${CR_REGISTRY}/${INIT_TAG}
DOCKER_BUILD=docker build ./ -f Dockerfile
DOCKER_PUSH=docker push
DOCKER_TAG=docker tag
DOCKER_RUN=docker run
VENV_VERSION_FOLDER := venv$(shell python3 --version | sed -ne 's/[^0-9]*\(\([0-9]*\.\)\{0,2\}\).*/\1/p' | sed -e "s/\.//g")

init-env: .PHONY
	pyenv local system 3.9.8 3.8.12 3.7.12
	pip3 install poetry
	poetry update

build: api-image alembic-init
api-image: .PHONY
	${DOCKER_BUILD} --target=app -t ${APP_TAG}
	${DOCKER_TAG} ${APP_TAG} ${APP_REPO_TAG}
	${DOCKER_PUSH} ${APP_REPO_TAG}

alembic-init:
	${DOCKER_BUILD} --target=init -t ${INIT_TAG}
	${DOCKER_TAG} ${INIT_TAG} ${INIT_REPO_TAG}
	${DOCKER_PUSH} ${INIT_REPO_TAG}

run:
	./scripts/local-run.sh

local-test: .PHONY
	poetry run tox -e py39-unit

done: .PHONY
	(\
		./scripts/deps-up.sh; \
		poetry run tox -e done; \
		./scripts/deps-dn.sh; \
	)
dev:
	poetry run uvicorn house_calendar.main:app --reload

.PHONY: