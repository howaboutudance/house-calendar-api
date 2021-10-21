from typing import Optional, Text
from datetime import datetime, timedelta
from pydantic import BaseModel, validator
from pydantic.fields import Field
from .config import HOUSE_CALENDAR_VERSION, START_TIME, help_get_version
from fastapi import __version__ as fastapi_version
from uvicorn import __version__ as uvicorn_version
import sys
from enum import Enum

class Location(BaseModel):
    name: Text = Field(..., max_length=200)
    address: Text

class BaseEvent(BaseModel):
    name: Text = Field(..., max_length=300)
    start_date: datetime = Field(None, description="Start time and date of the event")
    end_date: datetime = Field(None, description="End time and date of the event")
    duration: timedelta = Field(None, description="Duration (in seconds)")
    location: Location
    id: Optional[int]
    @validator('duration', pre=True, always=True)
    def default_duration(cls, v, *, values, **kwargs):
        return v or values['end_date'] - values['start_date']

class Event(BaseEvent):
    start_date: datetime = Field( 
        default=datetime.now(),
        description="Start time and date of the event")
    @validator('end_date', pre=True, always=True)
    def default_end_date(cls, v, *, values, **kwargs):
        return v or values['start_date'] + values["duration"]

class Status(BaseModel):
    alive:  Optional[bool] = Field(True)
    name: Optional[Text] = Field(
        f"House Music Calendar API {HOUSE_CALENDAR_VERSION} on Python {help_get_version()} - uvicorn {uvicorn_version}")
    python_version: Optional[Text] = Field(sys.version)
    fastapi_version: Optional[Text] = Field(fastapi_version)
    uvicorn_version: Optional[Text] = Field(uvicorn_version)
    start_time: Optional[Text] = Field(START_TIME)
    local_time: Optional[Text] = Field(datetime.now().isoformat())
