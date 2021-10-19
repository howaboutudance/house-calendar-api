from typing import List
from fastapi import Depends
from fastapi.param_functions import Path
from fastapi.responses import JSONResponse
from .events_dao import events_db, add_event_dao
from ..dependencies import ListParameters
from ..models import Event, BaseEvent
from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/")
async def add_event(event: BaseEvent):
    instance = add_event_dao(event)
    return JSONResponse({"instance": instance, "id": 1})

@router.get("/{id}", response_model=Event)
async def get_event(id: int) -> JSONResponse:
    results = [event for event in events_db if event["id"] == id]
    if len(results):
        resp = JSONResponse(results[0])
    else:
        resp = JSONResponse({}, status_code=404)
    return resp

@router.delete("/{id}")
async def delete_event(
    id: int = Path(..., title="ID of the event", ge=0)):
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


@router.get("/", response_model=List[Event])
async def get_event_list(
    list_parameters: ListParameters= Depends(ListParameters))-> JSONResponse:
    """
    Get Events List (with querying)
    """
    filter_keys = ["name", "start_date", "end_date", "id", "location"]
    # an inner function to make the resp query a little clearer
    def filter_location(k, v):
        if k != "location":
            return v
        else:
            return {loc_k: loc_v for (loc_k, loc_v) in v.items() if loc_k == "name"}

    resp = [
        {key:filter_location(key, value)
            for (key, value) 
            in event.items() 
            if key in filter_keys
        }  
        for event in events_db
    ][list_parameters.offset: list_parameters.limit]
    return JSONResponse(resp)
