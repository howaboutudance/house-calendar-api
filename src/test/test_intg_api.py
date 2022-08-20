# Copyright 2021 Michael Penhallegon 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import requests

pytestmark = pytest.mark.intergration

base_url = "http://127.0.0.1:8000"
def test_check_intergration_api_server_up():
    resp = requests.get("http://127.0.0.1:8000/docs")
    assert resp.status_code == 200

def test_itergration_event_list_status():
    resp = requests.get("http://127.0.0.1:8000/events/")
    assert resp.status_code == 200
    assert 'Content-type' in resp.headers

def test_integration_event_add(intg_event_single, caplog):
    test_event = intg_event_single
    resp = requests.post(f"{base_url}/events/", json=test_event)
    assert resp.status_code == 200
    assert 'Content-type' in resp.headers