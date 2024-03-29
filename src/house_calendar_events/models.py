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

from datetime import datetime, timedelta
from typing import List, Optional, Text

from pydantic import BaseModel, validator
from pydantic.fields import Field
from pydantic.types import UUID4

from house_calendar_events.config import APP_CONFIG


class ORMBaseModel(BaseModel):
    class Config(BaseModel.Config):  # type: ignore
        orm_mode = True


class LocationModel(ORMBaseModel):
    name: Text = Field(..., max_length=200)
    address: Text


class BaseEventModel(ORMBaseModel):
    id: Optional[UUID4]
    name: Text = Field(..., max_length=300)
    start_date: datetime = Field(None, description="Start time and date of the event")
    end_date: datetime = Field(None, description="End time and date of the event")
    duration: Optional[timedelta] = Field(
        0,
        description="Duration (in seconds)",
    )
    location: Optional[LocationModel]

    @validator("duration", pre=True, always=True)
    def default_duration(cls, v, *, values, **kwargs):
        duration = values["end_date"] - values["start_date"]
        return v or duration.seconds


class EventModel(BaseEventModel):
    start_date: datetime = Field(
        default=datetime.now(), description="Start time and date of the event"
    )


class StatusBaseModel(BaseModel):
    status: str = "OK"


class EventListStatusModel(StatusBaseModel):
    rows: List[EventModel]
    row_count: int


class EventStatusModel(StatusBaseModel):
    id: UUID4
    result: EventModel


class ErrorStatusModel(StatusBaseModel):
    error: str


class Status(BaseModel):
    alive: Optional[bool] = Field(True)
    name: Optional[Text] = Field(APP_CONFIG.get_openapi_name())
    python_version: Optional[Text] = Field(APP_CONFIG.SYS_VERSION)
    fastapi_version: Optional[Text] = Field(APP_CONFIG.FASTAPI_VERSION)
    uvicorn_version: Optional[Text] = Field(APP_CONFIG.UVICORN_VERSION)
    start_time: Optional[Text] = Field(APP_CONFIG.START_TIME)
    local_time: Optional[Text] = Field(datetime.now().isoformat())
