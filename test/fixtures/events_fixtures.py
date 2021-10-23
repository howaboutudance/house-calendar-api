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

from house_calendar import models as items
from datetime import datetime, timedelta
import pytest
from house_calendar.models import EventModel, Location

@pytest.fixture()
def location_fixture():
    return items.Location(name="Orient Express", address="123 4th ave S")

@pytest.fixture()
def event_valid_fixture(location_fixture):
    return  items.EventModel(name = "Event A", 
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

@pytest.fixture
def event_dao_fixture():

  return EventModel(
      name="Train Car House Party", start_date="2021-07-09T21:00", 
      end_date="2021-07-10T04:00", location=Location(
          name="Oriental Express",
          address = "123 Olive Way, Seattle, WA 98102"
      )
  )