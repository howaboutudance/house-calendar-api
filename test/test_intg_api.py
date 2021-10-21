import pytest
import requests

pytestmark = pytest.mark.intergration

base_url = "http://127.0.0.1:8000"
def test_check_intergration_api_server_up():
    resp = requests.get("http://127.0.0.1:8000/docs")
    assert resp.status_code == 200

@pytest.mark.skip
def test_itergration_event_list_status():
    resp = requests.get("http://127.0.0.1:8000/events/")
    assert resp.status_code == 200
    assert 'Content-type' in resp.headers

def test_integration_event_add(intg_event_single, caplog):
    test_event = intg_event_single
    resp = requests.post(f"{base_url}/events/", json=test_event)
    assert resp.status_code == 200
    assert 'Content-type' in resp.headers