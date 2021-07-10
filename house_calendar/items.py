from typing import Optional, Text
from datetime import datetime
from pydantic import BaseModel

class Location(BaseModel):
    name: Text
    address: Text

class Event(BaseModel):
    name: Text
    start_date: datetime
    end_date: datetime
    location: Location