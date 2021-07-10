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
COPY --from=builder /app/dist ./app/dist
WORKDIR /app
RUN pip3 install dist/house_calendar*
CMD python -m house_calendar