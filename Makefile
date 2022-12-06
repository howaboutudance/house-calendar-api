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

BASE_TAG = hematite/house-calendar-events
TEST_TAG = ${BASE_TAG}-test
APP_TAG = ${BASE_TAG}
INIT_TAG = ${BASE_TAG}-init
CR_REGISTRY = ghcr.io/howaboutudance
APP_REPO_TAG =  ${CR_REGISTRY}/${APP_TAG}
INIT_REPO_TAG = ${CR_REGISTRY}/${INIT_TAG}
DOCKER_BUILD=podman build ./ -f Dockerfile
DOCKER_PUSH=docker push
DOCKER_TAG=podman tag
DOCKER_RUN=docker run
VENV_VERSION_FOLDER := venv$(shell python3 --version | sed -ne 's/[^0-9]*\(\([0-9]*\.\)\{0,2\}\).*/\1/p' | sed -e "s/\.//g")

init-env: .PHONY
	pyenv local system 3.10.8 3.9.15 3.8.15
	pip3 install poetry
	poetry update

build: api-publish alembic-publish
api-image: .PHONY
	${DOCKER_BUILD} --target=app -t ${APP_TAG}
	${DOCKER_TAG} ${APP_TAG} ${APP_REPO_TAG}

api-publish: api-image
	${DOCKER_PUSH} ${APP_REPO_TAG}

alembic-init:
	${DOCKER_BUILD} --target=init -t ${INIT_TAG}
	${DOCKER_TAG} ${INIT_TAG} ${INIT_REPO_TAG}

alembic-publish: alembic-init
	${DOCKER_PUSH} ${INIT_REPO_TAG}

run:
	./scripts/local-run.sh

test: check .PHONY
	poetry run tox -e py310-unit

check:
	poetry run mypy src/house_calendar_events/ src/test
	poetry run black src
	poetry run isort src/house_calendar_events
	poetry run safety check -i 51457

done: run test .PHONY
	(\
		poetry run tox -e py310-intergration; \
		./scripts/podman-dn.sh; \
		podman pod stop app && podman pod rm app; \
	)
dev:
	(\
		cd src; \
		poetry run uvicorn house_calendar_events.api:app --reload; \
		cd ../; \
	)

.PHONY: