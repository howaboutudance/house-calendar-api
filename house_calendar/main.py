from starlette.responses import RedirectResponse
from house_calendar.routers import events
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .config import HOUSE_CALENDAR_VERSION, ORIGINS
from .datastore import locations_db, events_db
from .dependencies import ListParameters
from .routers import health, events

app = FastAPI(title="House Music Calendar", version=HOUSE_CALENDAR_VERSION)
app.include_router(health.router)
app.include_router(events.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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