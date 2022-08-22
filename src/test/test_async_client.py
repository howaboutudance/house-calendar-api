from httpx import AsyncClient
from house_calendar.api import app
import pytest

@pytest.mark.asyncio
async def test_async_client_create():
    async with AsyncClient(app=app) as ac:
        r = await ac.get("http://localhost/docs")
    assert r.status_code == 200

@pytest.mark.asyncio
async def test_async_client_fixutre(async_client):
    
    async with async_client as client:
        r = await client.get("http://localhost/docs")
        r.status_code = 200