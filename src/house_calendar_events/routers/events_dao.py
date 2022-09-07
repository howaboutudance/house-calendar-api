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

"""
events_dao create a series of function that models the Data Access Object
Pattern.
"""
import json
import logging
import uuid
from typing import Any, Mapping

from pydantic.error_wrappers import ValidationError
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import delete, select

from house_calendar_events.db.table_models import Event
from house_calendar_events.dependencies import ListParameters
from house_calendar_events.models import (BaseEventModel, ErrorStatusModel,
                                          EventListStatusModel, EventModel,
                                          EventStatusModel)


async def add_event_dao(
    event: BaseEventModel, session: AsyncSession
) -> EventStatusModel:
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
        location=event.location.dict(),  # type: ignore
    )
    session.add(table_entry)
    await session.flush()

    return EventStatusModel(
        status="OK", id=table_entry.id, result=EventModel.from_orm(table_entry)
    )


async def delete_event_dao(event_id: str, session: AsyncSession):
    """
    Deletes event by uuid id

    :param event_id: the id of the object to delete
    :param session: session to execute action in

    :raises ValueError: if row count is 0, (action had no effect)

    :returns: status, id parsed as string, and number of rows affected
    """
    parsed_id = uuid.UUID(event_id)
    query = delete(Event).where(Event.id == parsed_id)  # type: ignore
    result = await session.execute(query)
    result_rowcount: int = result.rowcount  # type: ignore
    if result_rowcount == 0:
        raise ValueError
    return {"status": "OK", "id": parsed_id.hex, "affected": result_rowcount}


async def get_event_list_dao(
    list_param: ListParameters, session: AsyncSession
) -> EventListStatusModel:
    """
    Get an event list in a JSON format

    :param list_param: parameters used to query values
    :param session: session to execute action in

    :returns: status, list of event entries and row_count
    """
    query = select(Event)  # type: ignore
    result = await session.execute(query)
    try:
        resp = [EventModel.from_orm(r) for r in result]
        return EventListStatusModel(rows=resp, row_count=len(resp))
    except ValidationError as e:
        logging.info(e)
        return EventListStatusModel(rows=[], row_count=0)


async def get_event_dao(event_id: str, session: AsyncSession) -> EventStatusModel:
    """
    Get event detail of one event

    :param event_id: the id of the event
    :param session: session to execute action in

    :returns: status and result
    """
    parsed_id = uuid.UUID(event_id)
    query = select(Event).where(Event.id == parsed_id)  # type: ignore
    result = (await session.execute(query)).one()
    if len(result) == 1:
        resp = EventModel.from_orm(result[0])
    return EventStatusModel(status="OK", id=resp.id, result=resp)
