# House Music Calendar Event Service

# Purpose

house_calendar_events is a the microservice to wrap and abstract the event db
postgres database. It handles basic CRUD interaction with Event and Locations.

# Endpoints

This microsservice is designed to handle basic CRUD operations of against
events, but also be a good  citizen for kubernetes/docker/podman with health
checks and statuses.

## Satus & Health Check Endpoints

## Event CRUD Endpoints

| Method | Endpoint    | Description                        |
|--------|-------------|------------------------------------|
| `GET`  | /event/     | A listing of events                |
| `GET`  | /event/{id} | Get individual event by uuid       |
| `POST` | /event/     | Create new event entry             |

# Local Development Environment

## Setting Configuration

## Alembic Migrations Rollout

# Project Structure