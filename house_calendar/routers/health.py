from ..items import Status
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse

router = APIRouter(tags=["health"])

@router.get("/pulse")
async def get_pulse() -> PlainTextResponse:
    return PlainTextResponse("OK") 

@router.get("/status")
async def get_status() -> Status:
    return Status()