from starlette.responses import RedirectResponse
from house_calendar.routers import events
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from .config import HOUSE_CALENDAR_VERSION
from .datastore import events_db, locations_db
from .dependencies import ListParameters
from .routers import health, events

app = FastAPI(title="House Music Calendar", version=HOUSE_CALENDAR_VERSION)
app.include_router(health.router)
app.include_router(events.router)

@app.get("/locations/", tags=["location"])
async def get_location_list(
    list_parameters: ListParameters = Depends(ListParameters)) -> JSONResponse:
    resp = [{
        **location, 
        "events": [
            {
                "name": event["name"],
                "start_date": event["start_date"],
                "end_date": event["end_date"],
                "id": event["id"]
            } for event in events_db
            if event["location"]["name"] == location["name"]
            ]}
        for location in locations_db
    ][list_parameters.offset:list_parameters.limit]
    return JSONResponse(resp)

@app.get("/")
def redirect_docs():
    return RedirectResponse("/docs")