import pytest
from house_calendar.main import app
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

def test_get_events():
  resp = client.get("/events/")
  assert resp.status_code == 200
  assert len(resp.json()) > 0

def test_post_events_invalid_entry():
  resp = client.post("/events/", {"foo": "bar"})
  assert resp.status_code == 422

def test_delete_events_valid():
  resp = client.delete("/events/2")
  assert resp.status_code == 200

def test_delete_events_invalid():
  resp = client.delete("/events/100")
  assert resp.status_code == 404

def test_post_events_valid_entry():
  expected_resp_keys = set(["instance", "id"])
  test_event = {
    "name": "Train Car House Party",
    "start_date": "2021-07-09T21:00",
    "end_date": "2021-07-10T04:00",
    "location": {
        "name": "Oriental Express",
        "address": "123 Olive Way, Seattle, WA 98102"
    }
  }
  resp = client.post("/events/", json=test_event)
  assert resp.status_code == 200
  assert expected_resp_keys <= set(resp.json().keys())

  def test_redirect_docs():
    resp = client.get("/")
    assert resp.status_code == 307

@pytest.mark.intergration
def test_itergration_status():
    assert True