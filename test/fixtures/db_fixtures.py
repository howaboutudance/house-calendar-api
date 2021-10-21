import pytest
import asyncio
from typing import Generator, Callable
from sqlalchemy.ext.asyncio import AsyncSession
from house_calendar.db.session import engine, async_session
from house_calendar.db.table_models import Base
from fastapi import FastAPI

@pytest.fixture
def mock_session():
    class MockSession():
        def add(self, obj):
            pass
        def commit(self, *args):
            pass
    
    return MockSession()

@pytest.fixture(scope="session")
def event_loop(request) -> Generator:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture()
async def db_session() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        async with async_session(bind=connection) as session:
            yield session
            await session.flush()
            await session.rollback()


@pytest.fixture()
def override_get_db(db_session: AsyncSession) -> Callable:
    async def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def app(override_get_db: Callable) -> FastAPI:
    from house_calendar.db import get_db
    from house_calendar.api import app

    app.dependency_overrides[get_db] = override_get_db
    return app