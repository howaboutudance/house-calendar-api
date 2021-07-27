from datetime import datetime
import house_calendar
from datetime import datetime
import sys

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