
from typing import List
from fastapi import Depends, FastAPI
from fastapi.param_functions import Path
from fastapi.responses import JSONResponse
from ..datastore import events_db
from ..dependencies import ListParameters
from ..items import Event, ExistingEvent
from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/")
async def add_event(event: Event):
    return {"instance": event, "id": 1}

@router.get("/{id}", response_model=ExistingEvent)
async def get_event(id: int) -> JSONResponse:
    results = [event for event in events_db if event["id"] == id]
    if len(results):
        return JSONResponse(results[0])
    else:
        return JSONResponse({}, status_code=404)

@router.delete("/{id}")
async def delete_event(
    id: int = Path(..., title="ID of the event", ge=0)) -> JSONResponse:
    if id in [event["id"] for event in events_db]:
        try:
            event_index = [event["id"] for event in events_db].index(id)
            del events_db[event_index]
        except IndexError as e:
            return JSONResponse({"error": e}, status_code=404)
        except ValueError as e:
            return JSONResponse({"error", e}, status_code=404)
    else:
        return JSONResponse({"message": f"{id} not found"}, status_code=404)


@router.get("/", response_model=List[ExistingEvent])
async def get_event_list(
    list_parameters: ListParameters= Depends(ListParameters))-> JSONResponse:
    """
    Get Events List (with querying)
    """
    filter_keys = ["name", "start_date", "end_date", "id"]
    resp = [
        {key:value
            for (key, value) 
            in event.items() 
            if key in filter_keys
        }  
        for event in events_db
    ][list_parameters.offset: list_parameters.limit]
    return JSONResponse(resp)
