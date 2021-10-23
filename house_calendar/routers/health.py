from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse, JSONResponse
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
    return JSONResponse({"status": "ok", 
    "client": {'address': request.client}})