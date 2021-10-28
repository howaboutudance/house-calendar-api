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

"""
events_dao create a series of function that models the Data Access Object
Pattern.
"""
import uuid

from typing import Mapping, Any
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import delete, select

from ..db.table_models import Event
from ..models import BaseEventModel, EventModel
from ..dependencies import ListParameters


async def add_event_dao(event: BaseEventModel, session: AsyncSession) -> Mapping[str, Any]:
    """
    Creates new objects in the database

    :param event: the event to be added
    :returns: a dict with the added event's id and the resulting object
    """
    table_entry = Event(
        id=uuid.uuid4(), 
        name=event.name,
        start_date=event.start_date,
        end_date=event.end_date,
        location=event.location.dict()
        )
    session.add(table_entry)
    return {"status": "OK", "id": table_entry.id, 
        "result": EventModel.from_orm(table_entry)}


async def delete_event_dao(event_id: str, session: AsyncSession):
    """
    Deletes event by uuid id

    :param event_id: the id of the object to delete
    :param session: session to execute action in

    :raises ValueError: if row count is 0, (action had no effect)

    :returns: status, id parsed as string, and number of rows affected
    """
    parsed_id = uuid.UUID(event_id)
    query = delete(Event).where(Event.id==parsed_id)
    result = await session.execute(query)
    result_rowcount: int = result.rowcount #type: ignore
    if result_rowcount == 0:
        raise ValueError
    return {"status": "OK", "id": parsed_id.hex, "affected": result_rowcount}


async def get_event_list_dao(list_param: ListParameters, session: AsyncSession):
    """
    Get an event list in a JSON format

    :param list_param: parameters used to query values
    :param session: session to execute action in

    :returns: status, list of event entries and row_count
    """
    query = select(Event)
    result = await session.execute(query)
    resp_list = [EventModel.from_orm(r).json() for r in result]
    return {"status":"OK", "rows": resp_list, "row_count": len(resp_list)}

async def get_event_dao(event_id: str, session: AsyncSession):
    """
    Get event detail of one event

    :param event_id: the id of the event
    :param session: session to execute action in

    :returns: status and result
    """
    parsed_id = uuid.UUID(event_id)
    query = select(Event).where(Event.id == parsed_id)
    result = (await session.execute(query)).one()
    if len(result) == 1:
        resp = EventModel.from_orm(result[0])
    else:
        raise ValueError
    return {"status": "OK", "result": resp.json()}
