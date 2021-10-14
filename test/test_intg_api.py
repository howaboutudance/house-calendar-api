import pytest
import requests

@pytest.mark.intergration
def test_check_intergration_api_server_up():
    resp = requests.get("http://127.0.0.1:8000/docs")
    assert resp.status_code == 200

@pytest.mark.intergration
def test_itergration_event_list_status():
    resp = requests.get("http://127.0.0.1:8000/events/")
    assert resp.status_code == 200
    assert 'Content-type' in resp.headers