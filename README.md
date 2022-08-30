# House Music Calendar Event Service

# Purpose

house_calendar_events is a the microservice to wrap and abstract the event db
postgres database. It handles basic CRUD interaction with Event and Locations.

# Endpoints

This microsservice is designed to handle basic CRUD operations of against
events, but also be a good  citizen for kubernetes/docker/podman with health
checks and statuses.

## Satus & Health Check Endpoints

| Method  | Endpoint    | Description                        |
|---------|-------------|------------------------------------|
| `GET`   | /pulse/     | Basic binary canary "OK" if good   |
| `GET`   | /status/    | Status response                    |

## Event CRUD Endpoints

| Method  | Endpoint    | Description                        |
|---------|-------------|------------------------------------|
| `GET`   | /event/     | A listing of events                |
| `POST`  | /event/     | Create new event entry             |
| `GET`   | /event/{id} | Get individual event by uuid       |
| `DELETE`| /event/{id} | Delete individual event by uuid    | 

# Local Development Environment

## Setting Configuration

## Alembic Migrations Rollout

## Intialization

# Project Structure

# Development Workflow