from house_calendar.routers.events_dao import add_event_dao, delete_event_dao
import pytest
from house_calendar.models import Event, Location

@pytest.fixture
def event_fixture():

  return Event(
      name="Train Car House Party", start_date="2021-07-09T21:00", 
      end_date="2021-07-10T04:00", location=Location(
          name="Oriental Express",
          address = "123 Olive Way, Seattle, WA 98102"
      )
  )
def test_add_event_dao(caplog, event_fixture):
    test_event = event_fixture
    result = add_event_dao(test_event)
    assert type(result) is dict