# Copyright 2021 Michael Penhallegon 
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

from fastapi import Depends, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import Union

from .location_dao import get_location_list_dao
from ..db.session import get_db
from ..dependencies import ListParameters
from ..models import ErrorStatusModel, LocationListStatusModel

router = APIRouter(prefix="/locations", tags=["location"])

log = logging.getLogger(__name__)


# TODO: make seperate router and build out dao/schemas/tables 
@router.get("/", tags=["location"])
async def get_location_list(response: Response,
    list_parameters: ListParameters = Depends(ListParameters),
    session: AsyncSession = Depends(get_db)) -> Union[ErrorStatusModel, LocationListStatusModel]:
    try:
        return await get_location_list_dao(session)
    except ValueError as e:
        return ErrorStatusModel(status="ERROR", error=str(e))