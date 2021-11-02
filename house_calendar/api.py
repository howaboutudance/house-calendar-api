# Copyright 2021 Michael Penhallegon 
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
import time

from typing import Callable
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from .config import APP_CONFIG 
from .routers import health, events, location


app = FastAPI(title="House Music Calendar", version=APP_CONFIG.HOUSE_CALENDAR_VERSION)
app.include_router(health.router)
app.include_router(events.router)
app.include_router(location.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=APP_CONFIG.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


log = logging.getLogger(__name__)


@app.on_event("startup")
async def start_worker():
    log.info("Starting house_calendar api service...")


@app.on_event("shutdown")
async def stop_instance():
    log.info("Stopping house_calendar api service...")


@app.middleware("http")
async def push_to_promethesu(request: Request, call_next: Callable):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    response.headers["X-process-time"] = f"{process_time} ms"
    return response


@app.get("/")
def redirect_docs():
    return RedirectResponse("/docs")