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

BASE_TAG = hematite/house_calendar_api
TEST_TAG = ${BASE_TAG}-test
DOCKER_BUILD=docker build ./ -f Dockerfile
DOCKER_RUN=docker run
VENV_VERSION_FOLDER := venv$(shell python3 --version | sed -ne 's/[^0-9]*\(\([0-9]\.\)\{0,2\}\).*/\1/p' | sed -e "s/\.//g")

init-env: FORCE
	pyenv local 3.9.6 3.7.11 3.8.11
	python3 -m venv ./$(VENV_VERSION_FOLDER)
	( \
		source ./$(VENV_VERSION_FOLDER)/bin/activate; \
		pip3 install --use-feature=2020-resolver -r requirements.txt; \
		pip3 install --use-feature=2020-resolver -r requirements-dev.txt; \
	)

build: FORCE
	${DOCKER_BUILD} --no-cache=true --target=app -t ${BASE_TAG}

run:
	${DOCKER_RUN} -p 8000:8000 ${BASE_TAG}

test: FORCE
	${DOCKER_BUILD} --target=test -t ${INTERACT_TAG}
	${DOCKER_RUN} -it ${INTERACT_TAG}

local-test: FORCE
	tox -e py39-unit
	mypy house_calendar

dev:
	uvicorn house_calendar.main:app --reload

FORCE: