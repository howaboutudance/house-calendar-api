import pytest
from unittest.mock import patch
from house_calendar.api import app
from fastapi.testclient import TestClient
from httpx import AsyncClient
client = TestClient(app)

def test_pulse():
  resp = client.get("/pulse")
  assert resp.status_code == 200
  assert resp.text == "OK"

def test_status():
  expected_keys = set(["name", "python_version", "uvicorn_version", 
    "fastapi_version"])
  resp = client.get("/status")
  assert resp.status_code == 200
  assert  expected_keys <= set(resp.json().keys())

def test_get_events():
  resp = client.get("/events/")
  assert resp.status_code == 200
  assert len(resp.json()) > 0

@pytest.mark.asyncio
async def test_post_events_invalid_entry(async_client):
  resp = await async_client.post("/events/", json={"foo": "bar"})
  assert resp.status_code == 422

def test_delete_events_valid():
  resp = client.delete("/events/2")
  assert resp.status_code == 200

def test_delete_events_invalid():
  resp = client.delete("/events/100")
  assert resp.status_code == 404

@pytest.mark.asyncio
async def test_post_events_valid_entry(event_post_fixture, async_client, db_session):
  test_event = event_post_fixture
  expected_resp_keys = set(["instance", "id"])
  resp = await async_client.post("/events/", json=test_event)
  assert resp.status_code == 200
  assert expected_resp_keys <= set(resp.json().keys())

def test_redirect_docs():
  resp = client.get("/")
  assert resp.status_code == 200