from typing import MutableMapping

import uuid
from sqlalchemy.ext.asyncio.session import AsyncSession
from house_calendar.db.table_models import EventTable
from ..datastore import inc_event_id, events_db
from ..models import BaseEvent


def add_event_dao(event: BaseEvent, session: AsyncSession) -> EventTable:
    table_entry = EventTable(
        id=uuid.uuid4(), 
        name=event.name,
        start_date=event.start_date,
        end_date=event.end_date
        )
    session.add(table_entry)
    return table_entry


def delete_event_dao(event: BaseEvent):
    return {"status": "OK"}