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

from typing import Union, List, Dict, Text
from datetime import datetime as DateTime
from uuid import UUID
## Tyoe Definitions
JSONSingleton = Union[Text, int, float, bool]
JSONType = Union[JSONSingleton, List['JSONType'], Dict[Text, 'JSONType']] # type: ignore

def create_iso_date(*args) -> Text:
    return DateTime(*args).isoformat()

def is_uuid(id: str) -> bool:
    try:
        UUID(id)
        return True
    except TypeError:
        return False