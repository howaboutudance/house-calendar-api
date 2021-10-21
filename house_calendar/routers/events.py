from typing import List
from fastapi import Depends
from fastapi.param_functions import Path
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio.session import AsyncSession

from house_calendar.db.session import get_db
from house_calendar.db.table_models import EventTable
from .events_dao import delete_event_dao, add_event_dao
from ..dependencies import ListParameters
from ..models import Event, BaseEvent
from fastapi import APIRouter
import uuid

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/")
async def add_event(event: BaseEvent, session: AsyncSession = Depends(get_db)):
    result = await add_event_dao(event, session) 
    return JSONResponse({"id": str(result["id"])})

@router.get("/{id}", response_model=Event)
async def get_event(id: int) -> JSONResponse:
    # results = [event for event in events_db if event["id"] == id]
    resp = JSONResponse([])
    # else:
    #     resp = JSONResponse({}, status_code=404)
    return resp

@router.delete("/{id}")
async def delete_event(
    id: str,
    session: AsyncSession = Depends(get_db)):
    try:
        action_response = await delete_event_dao(id, session)
        return JSONResponse(action_response, status_code=200)
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=404)


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
