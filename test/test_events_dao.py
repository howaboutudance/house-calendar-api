import pytest
from house_calendar.routers.events_dao import add_event_dao, delete_event_dao
from house_calendar.models import Event

pytestmark = pytest.mark.asyncio

async def test_add_event_dao(caplog, event_dao_fixture, db_session):
    test_session = db_session
    test_event = event_dao_fixture
    result = await add_event_dao(test_event, test_session)
    assert type(result["result"]) is Event

async def test_delete_event_ado(caplog, event_dao_fixture, db_session):
    test_session = db_session
    test_event = event_dao_fixture
    add_result = await add_event_dao(test_event, test_session)
    result = await delete_event_dao(str(add_result["id"].hex), test_session)
    assert "affected" in result
    assert 0 == result["affected"]