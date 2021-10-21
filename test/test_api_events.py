import pytest

pytestmark = pytest.mark.asyncio

async def test_post_events_invalid_entry(async_client):
  resp = await async_client.post("/events/", json={"foo": "bar"})
  assert resp.status_code == 422

async def test_post_events_valid_entry(event_post_fixture, async_client, db_session):
  test_event = event_post_fixture
  expected_resp_keys = set(["instance", "id"])
  resp = await async_client.post("/events/", json=test_event)
  assert resp.status_code == 200
  assert expected_resp_keys <= set(resp.json().keys())

async def test_delete_events_valid(async_client, db_session):
  resp = await async_client.delete("/events/00010203-0405-0607-0809-0a0b0c0d0e0f")
  assert resp.status_code == 200

async def test_delete_events_invalid(async_client, db_session):
  resp = await async_client.delete("/events/100")
  assert resp.status_code == 404