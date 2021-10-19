from ..datastore import inc_event_id, events_db
from ..models import BaseEvent
def add_event_dao(event: BaseEvent):
    id = inc_event_id()
    events_db.append({**event.dict(), "id": id})
    return {"status": "OK", "id": id}

def delete_event_dao(event: BaseEvent):
    return {"status": "OK"}