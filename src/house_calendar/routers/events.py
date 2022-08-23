# Copyright 2021-2022 Michael Penhallegon 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from typing import List, Union

from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.sqltypes import JSON

from ..db.session import get_db
from ..dependencies import ListParameters
from ..models import (BaseEventModel, ErrorStatusModel, EventListStatusModel,
                      EventStatusModel)
from .events_dao import (add_event_dao, delete_event_dao, get_event_dao,
                         get_event_list_dao)

router = APIRouter(prefix="/events", tags=["events"])

log = logging.getLogger(__name__)

@router.post("/")
async def add_event(event: BaseEventModel, session: AsyncSession = Depends(get_db)):
    result = await add_event_dao(event, session) 
    return result

@router.get("/{id}", response_model=EventStatusModel)
async def get_event(id: str,
    session: AsyncSession = Depends(get_db)) -> Union[EventStatusModel, ErrorStatusModel]:
    try:
        resp = await get_event_dao(id, session)
        return resp
    except ValueError as e:
       return ErrorStatusModel(error=e, status="ERROR")

@router.delete("/{id}")
async def delete_event(id: str, response: Response,
    session: AsyncSession = Depends(get_db)) -> JSONResponse:
    try:
        action_response = await delete_event_dao(id, session)
        return JSONResponse(action_response, status_code=200)
    except ValueError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse({"error": str(e)}, status_code=404)


@router.get("/")
async def get_event_list(response: Response,
    list_parameters: ListParameters= Depends(ListParameters),
    session: AsyncSession = Depends(get_db))-> Union[EventListStatusModel, ErrorStatusModel]:
    """
    Get Events List (with querying)
    """
    filter_keys = ["name", "start_date", "end_date", "id", "location"]
    try:
        resp = await get_event_list_dao(list_parameters, session)
        return resp
    except ValueError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorStatusModel(status="ERROR", error=str(e))
