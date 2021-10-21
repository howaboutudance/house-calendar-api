import pytest
import datetime
from typing import Text

def _create_iso_date(*args) -> Text:
    return datetime.datetime(*args).isoformat()

# @pytest.fixture()
def intg_event_single():
    location = {"name": "Monkey Loft",
        "address": "2915 1st Ave S, Seattle, WA 98134"}
    event = {"name":"Habitat", "start_date": _create_iso_date(2021, 7, 14, 21),
    "end_date": _create_iso_date(2021, 7, 15, 4), "location": location}
    return event