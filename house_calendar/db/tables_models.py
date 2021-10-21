from typing import Text
from sqlalchemy import Index, ForeignKey, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql.schema import Sequence
import uuid

from sqlalchemy.sql.sqltypes import JSON, DateTime, String

@as_declarative()
class Base():
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    __name__: str
    @declared_attr
    def __tablename__(cls) -> Text:
        return cls.__name__.lower()

class EventTable(Base):
    __tablename__ = "event"
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    # TODO: figure out how to convert from timdelta
    # duration = Column(String)
    # TODO: research how to convert model to JSON
    # location = Column(JSON)