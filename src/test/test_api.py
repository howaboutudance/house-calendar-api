# Copyright 2021-2022 Michael Penhallegon
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

from unittest.mock import patch
from house_calendar.api import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_pulse():
    resp = client.get("/pulse")
    assert resp.status_code == 200
    assert resp.text == "OK"


def test_status():
    expected_keys = set(
        ["name", "python_version", "uvicorn_version", "fastapi_version"]
    )
    resp = client.get("/status")
    assert resp.status_code == 200
    assert expected_keys <= set(resp.json().keys())


def test_redirect_docs():
    resp = client.get("/")
    assert resp.status_code == 200
