BASE_TAG = hematite/house_church_api
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
	${DOCKER_RUN} ${BASE_TAG}

test: FORCE
	${DOCKER_BUILD} --target=test -t ${INTERACT_TAG}
	${DOCKER_RUN} -it ${INTERACT_TAG}

local-test: FORCE
	tox -e py39-unit
	mypy house_calendar

dev:
	uvicorn house_calendar.main:app --reload

FORCE: