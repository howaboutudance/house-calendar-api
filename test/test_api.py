import pytest

from unittest.mock import patch
from house_calendar.api import app
from fastapi.testclient import TestClient


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


def test_redirect_docs():
  resp = client.get("/")
  assert resp.status_code == 200