from typing import Optional, Text
from datetime import datetime
from pydantic import BaseModel
from pydantic.fields import Field
from .config import HOUSE_CALENDAR_VERSION, START_TIME, help_get_version
from fastapi import FastAPI, __version__ as fastapi_version
from uvicorn import __version__ as uvicorn_version
import sys
class Location(BaseModel):
    name: Text = Field(..., max_length=200)
    address: Text

class Event(BaseModel):
    name: Text = Field(..., max_length=300)
    start_date: datetime = Field( 
        default=datetime.now(),
        description="Start time and date of the event")
    end_date: datetime = Field(
        default=datetime.now(),
        description="End time/date of the event"
    )
    location: Location

class ExistingEvent(Event):
    id: int

class Status(BaseModel):
    alive:  Optional[bool] = Field(True)
    name: Optional[Text] = Field(f"House Music Calendar API {HOUSE_CALENDAR_VERSION} on Python {help_get_version()} - uvicorn {uvicorn_version}")
    python_version: Optional[Text] = Field(sys.version)
    fastapi_version: Optional[Text] = Field(fastapi_version)
    uvicorn_version: Optional[Text] = Field(uvicorn_version)
    start_time: Optional[Text] = Field(START_TIME)
    local_time: Optional[Text] = Field(datetime.now().isoformat())
