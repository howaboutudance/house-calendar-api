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

@pytest.mark.skip
def test_get_events():
  resp = client.get("/events/")
  assert resp.status_code == 200
  assert len(resp.json()) > 0

def test_redirect_docs():
  resp = client.get("/")
  assert resp.status_code == 200