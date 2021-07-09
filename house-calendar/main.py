from typing import Optional, Text
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from .health import Status
app = FastAPI()

class Location(BaseModel):
    name: Text

class Event(BaseModel):
    name: Text
    start_date: datetime
    end_date: datetime
    location: Location


@app.post("/events/")
def add_event(event: Event) -> JSONResponse:
    return JSONResponse({"message":"ok", "id": 0})

@app.get("/events/{id}")
def get_event(id: int) -> JSONResponse:
    return JSONResponse({"message": "ok"})

@app.get("/events")
def get_event_list() -> JSONResponse:
    return JSONResponse([{"event": 1, "name": "hello"}])

@app.get("/status")
def get_status() -> JSONResponse:
    return JSONResponse({"message": "fail"})