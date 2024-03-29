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

from httpx import AsyncClient
from house_calendar_events.api import app
import pytest


@pytest.mark.asyncio
async def test_async_client_create():
    async with AsyncClient(app=app) as ac:
        r = await ac.get("http://localhost/docs")
    assert r.status_code == 200


@pytest.mark.asyncio
async def test_async_client_fixture(async_client):

    async with async_client as client:
        r = await client.get("http://localhost/docs")
        r.status_code = 200
