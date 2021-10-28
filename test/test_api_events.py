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

from typing import Awaitable
import pytest
import uuid
from house_calendar.util import is_uuid


pytestmark = pytest.mark.asyncio


async def test_post_event_invalid_entry(async_client):
  resp = await async_client.post("/events/", json={"foo": "bar"})
  assert resp.status_code == 422


async def test_post_event_valid_entry(event_post_fixture, async_client, db_session):
  test_event = event_post_fixture
  #TODO: update after changing parsing of EventModel to handle uuid -> string
  expected_resp_keys = set(["id"])
  resp = await async_client.post("/events/", json=test_event)
  assert resp.status_code == 200
  
  resp_json = resp.json()
  assert expected_resp_keys <= set(resp_json.keys())
  assert is_uuid(resp_json["id"])


async def test_delete_event_invalid(async_client, db_session):
  resp = await async_client.delete("/events/100")
  assert resp.status_code == 404


async def test_delete_event_valid(async_client, db_session, event_with_uuid_fixture):
  add_event = await async_client.post("/events/", json=event_with_uuid_fixture)
  assert add_event.status_code == 200
  add_event_json = add_event.json()
  assert is_uuid(add_event_json["id"])

  resp = await async_client.delete("/events/{id}".format(id=add_event_json["id"]))
  assert resp.status_code == 200

  resp_json = resp.json()
  assert 1 >= resp_json["affected"]

async def test_get_event(caplog, async_client, db_session, event_with_uuid_fixture):
  add_event = await async_client.post("/events/", json=event_with_uuid_fixture)
  assert add_event.status_code == 200
  add_event_uuid = add_event.json()["id"]
  assert is_uuid(add_event_uuid)

  resp = await async_client.get(f"/events/{add_event_uuid}")
  assert resp.status_code == 200
  resp_json = resp.json()
  assert "error" not in resp_json

@pytest.mark.skip
async def test_get_events(async_client, db_session):
  resp = async_client.get("/events/")
  assert resp.status_code == 200
  assert len(resp.json()) > 0