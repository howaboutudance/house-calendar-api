from datetime import datetime
from posix import environ
import house_calendar
from datetime import datetime
import sys
import os
from dataclasses import dataclass

HOUSE_CALENDAR_VERSION = "dev"

try:
    HOUSE_CALENDAR_VERSION = house_calendar.__version__
except AttributeError:
    print("using dev")

START_TIME = datetime.isoformat(datetime.now())
ORIGINS = [
    "http://localhost",
    "http://localhost:3000"
]
def help_get_version():
    vers = sys.version_info
    python_version = ".".join([str(x) for x in [vers.major, vers.minor, vers.micro]])
    return python_version

@dataclass
class db_config():
    ENGINE_URI = os.environ.get("POSTGRES_URI") if "POSTGRES_URI" in os.environ  else "postgresql+asyncpg://admin:500boylston@127.0.0.1:5432/house_calendar_events"

DB_CONFIG = db_config()
