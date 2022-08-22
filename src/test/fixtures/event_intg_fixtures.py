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

import pytest
import datetime
from typing import Text

def _create_iso_date(*args) -> Text:
    return datetime.datetime(*args).isoformat()

@pytest.fixture()
def intg_event_single():
    location = {"name": "Monkey Loft",
        "address": "2915 1st Ave S, Seattle, WA 98134"}
    event = {"name":"Habitat", "start_date": _create_iso_date(2021, 7, 14, 21),
    "end_date": _create_iso_date(2021, 7, 15, 4), "location": location}
    return event