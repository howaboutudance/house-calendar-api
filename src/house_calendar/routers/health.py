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

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, PlainTextResponse

from ..models import Status

router = APIRouter(tags=["health"])


@router.get("/pulse")
async def get_pulse() -> PlainTextResponse:
    return PlainTextResponse("OK")


@router.get("/status")
async def get_status() -> Status:
    return Status()


@router.get("/metrics")
async def get_metrics(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok", "client": {"address": request.client}})
