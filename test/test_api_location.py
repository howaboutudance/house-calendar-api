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
from typing import List

pytestmark = pytest.mark.asyncio

async def test_location_get(async_client, db_session):
    resp = await async_client.get("/locations/")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert "rows" in resp_json
    assert isinstance(resp_json["rows"], List)
    assert "row_count" in resp_json