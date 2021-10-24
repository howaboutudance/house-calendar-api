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
  assert expected_resp_keys <= set(resp.json().keys())


async def test_delete_event_invalid(async_client, db_session):
  resp = await async_client.delete("/events/100")
  assert resp.status_code == 404


async def test_delete_event_valid(async_client, db_session):
  resp = await async_client.delete("/events/00010203-0405-0607-0809-0a0b0c0d0e0f")
  assert resp.status_code == 200


@pytest.mark.skip
def test_get_events():
  resp = client.get("/events/")
  assert resp.status_code == 200
  assert len(resp.json()) > 0