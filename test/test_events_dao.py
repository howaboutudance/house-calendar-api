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
from house_calendar.routers.events_dao import add_event_dao, delete_event_dao, get_event_list_dao
from house_calendar.models import EventModel
from house_calendar.dependencies import ListParameters

pytestmark = pytest.mark.asyncio

async def test_add_event_dao(caplog, event_dao_fixture, db_session):
    test_session = db_session
    test_event = event_dao_fixture
    result = await add_event_dao(test_event, test_session)
    assert type(result.result) is EventModel

async def test_delete_event_dao(caplog, event_dao_fixture, db_session):
    test_session = db_session
    test_event = event_dao_fixture
    add_result = await add_event_dao(test_event, test_session)
    result = await delete_event_dao(add_result.id.hex, test_session)
    assert "affected" in result
    assert 1 == result["affected"]

async def test_delete_event_dao_raise_on_nil_uuid(caplog, db_session):
    test_session = db_session
    with pytest.raises(ValueError):
        result = await delete_event_dao("00000000-0000-0000-0000-000000000000", test_session)

async def test_get_event_list_dao(caplog, db_session):
    test_session = db_session
    list_params = ListParameters()
    result = await get_event_list_dao(list_params, test_session)
    assert type(result.rows) is list