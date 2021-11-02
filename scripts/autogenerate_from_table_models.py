#/bin/bash
docker run -p 5432:5432 -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=hc_events \
    -d --name alembic_migrate_db postgres
export POSTGRES_MIGRATE_URI=postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/hc_events; \
    alembic revision --autogenerate -m "$(1)"
docker stop alembic_migrate_db