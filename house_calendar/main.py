from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .routers.health import Status
from .items import Event
import house_calendar
import datetime

app = FastAPI()


@app.post("/events/")
async def add_event(event: Event) -> JSONResponse:
    return {"instance": event, "id": 1}

@app.get("/events/{id}")
async def get_event(id: int) -> JSONResponse:
    return {"message": "ok"}

@app.get("/events")
async def get_event_list() -> JSONResponse:
    return [{"event": 1, "name": "hello"}]

@app.get("/pulse")
async def get_pulse() -> JSONResponse:
    return "OK" 

@app.get("/status")
async def get_status() -> JSONResponse:
    content = {
        "name": f"House Music Calendar API",
        "local_time": f"{datetime.datetime.now()}"
    }
    return JSONResponse(content)
