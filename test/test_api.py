import pytest
from house_calendar.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_pulse():
  resp = client.get("/pulse")
  assert resp.status_code == 200

@pytest.mark.intergration
def test_status():
    assert True