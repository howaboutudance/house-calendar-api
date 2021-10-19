from house_calendar import models as items
from datetime import datetime, timedelta
import pytest

@pytest.fixture()
def location_fixture():
    return items.Location(name="Orient Express", address="123 4th ave S")

@pytest.fixture()
def event_valid_fixture(location_fixture):
    return  items.Event(name = "Event A", 
        start_date=datetime(2021, 7, 27, 20), end_date=datetime(2021, 7, 28, 1),
        location=location_fixture)

@pytest.fixture
def event_post_fixture():

  return {
    "name": "Train Car House Party",
    "start_date": "2021-07-09T21:00",
    "end_date": "2021-07-10T04:00",
    "location": {
        "name": "Oriental Express",
        "address": "123 Olive Way, Seattle, WA 98102"
    }
  }