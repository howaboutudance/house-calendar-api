import uuid

from typing import Mapping, Any
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import delete, select

from ..db.table_models import Event
from ..models import BaseEventModel, EventModel


async def add_event_dao(event: BaseEventModel, session: AsyncSession) -> Mapping[str, Any]:
    table_entry = Event(
        id=uuid.uuid4(), 
        name=event.name,
        start_date=event.start_date,
        end_date=event.end_date,
        location=event.location.dict()
        )
    session.add(table_entry)
    return {"id": table_entry.id, "result": EventModel.from_orm(table_entry)}


async def delete_event_dao(event_id: str, session: AsyncSession):
    parsed_id = uuid.UUID(event_id)
    query = delete(Event).where(Event.id==parsed_id)
    result = await session.execute(query)
    return {"status": "OK", "id": parsed_id.hex, "affected": result.rowcount}


async def get_events_dao(session: AsyncSession):
    query = select(Event)
    result = await session.execute(query)
    return {"status":"OK", "rows": EventModel.from_orm(result)}