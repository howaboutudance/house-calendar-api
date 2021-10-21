from typing import Mapping, MutableMapping

import uuid
from typing import Any
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import delete, select
from house_calendar.db.table_models import EventTable
from ..models import BaseEvent, Event


async def add_event_dao(event: BaseEvent, session: AsyncSession) -> Mapping[str, Any]:
    table_entry = EventTable(
        id=uuid.uuid4(), 
        name=event.name,
        start_date=event.start_date,
        end_date=event.end_date,
        location=event.location.dict()
        )
    session.add(table_entry)
    return {"id": table_entry.id, "result": Event.from_orm(table_entry)}


async def delete_event_dao(event_id: str, session: AsyncSession):
    parsed_id = uuid.UUID(event_id)
    query = delete(EventTable).where(EventTable.id==parsed_id)
    result = await session.execute(query)
    return {"status": "OK", "id": parsed_id.hex, "affected": result.rowcount}

async def get_events_dao(session: AsyncSession):
    query = select(EventTable)
    result = await session.execute(query)
    return {"status":"OK", "rows": Event.from_orm(result)}