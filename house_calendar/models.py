from typing import Optional, Text
from datetime import datetime, timedelta
from pydantic import BaseModel, validator
from pydantic.fields import Field
from pydantic.types import UUID4
from .config import APP_CONFIG

class ORMBaseModel(BaseModel):
    class Config(BaseModel.Config):
        orm_mode = True

class LocationModel(ORMBaseModel):
    name: Text = Field(..., max_length=200)
    address: Text

class BaseEventModel(ORMBaseModel):
    id: Optional[UUID4]
    name: Text = Field(..., max_length=300)
    start_date: datetime = Field(None, description="Start time and date of the event")
    end_date: datetime = Field(None, description="End time and date of the event")
    duration: timedelta = Field(None, description="Duration (in seconds)")
    location: LocationModel
    @validator('duration', pre=True, always=True)
    def default_duration(cls, v, *, values, **kwargs):
      return v or values['end_date'] - values['start_date']

class EventModel(BaseEventModel):
    start_date: datetime = Field( 
        default=datetime.now(),
        description="Start time and date of the event")

class Status(BaseModel):
    alive:  Optional[bool] = Field(True)
    name: Optional[Text] = Field(APP_CONFIG.get_openapi_name())
    python_version: Optional[Text] = Field(APP_CONFIG.SYS_VERSION)
    fastapi_version: Optional[Text] = Field(APP_CONFIG.FASTAPI_VERSION)
    uvicorn_version: Optional[Text] = Field(APP_CONFIG.UVICORN_VERSION)
    start_time: Optional[Text] = Field(APP_CONFIG.START_TIME)
    local_time: Optional[Text] = Field(datetime.now().isoformat())
