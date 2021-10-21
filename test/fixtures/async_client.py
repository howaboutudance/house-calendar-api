from typing import AsyncGenerator

import pytest
from fastapi import FastAPI

from httpx import AsyncClient

@pytest.fixture()
async def async_client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        yield ac