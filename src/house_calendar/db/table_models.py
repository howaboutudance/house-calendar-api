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

import uuid

from typing import Text
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy.sql.sqltypes import DateTime, String, Integer


@as_declarative()
class Base():
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    __name__: str

    def __init__(self, *args, **kwargs) -> None:
        ...

    @declared_attr
    def __tablename__(cls) -> Text:
        return cls.__name__.lower()


class Event(Base):
    __name__ = "event"
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    duration = Column(Integer)
    location = Column(JSONB)