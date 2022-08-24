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

import logging
import os
import sys
from dataclasses import dataclass
from datetime import datetime as Datetime

from dynaconf import Dynaconf
from fastapi import __version__ as fastapi_version
from uvicorn import __version__ as uvicorn_version

import house_calendar

log = logging.getLogger(__name__)

settings = Dynaconf(
    envvar_prefix="HOUSE_CALENDAR_EVENTS",
    settings_files=['settings.toml', '.secrets.toml'],
    environments=True
)


@dataclass(frozen=True)
class APP_CONFIG():
    START_TIME = Datetime.isoformat(Datetime.now())

    if "__version__" in dir(house_calendar):
        try:
            HOUSE_CALENDAR_VERSION = house_calendar.__version__
        except AttributeError:
            HOUSE_CALENDAR_VERSION = "dev"
        finally:
            log.info(f"using {HOUSE_CALENDAR_VERSION}")

    PYTHON_VERSION = (lambda vers: f"{vers.major}.{vers.minor}.{vers.micro}")(sys.version_info)

    ORIGINS = settings.origins 
    UVICORN_VERSION = uvicorn_version
    FASTAPI_VERSION = fastapi_version
    SYS_VERSION = sys.version
    @classmethod
    def get_openapi_name(cls):
        return f"House Music Calendar API {cls.HOUSE_CALENDAR_VERSION} on Python {cls.PYTHON_VERSION} - uvicorn {uvicorn_version}"
    