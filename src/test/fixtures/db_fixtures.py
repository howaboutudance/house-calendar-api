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

import pytest
import pytest_asyncio
from typing import AsyncGenerator, Generator, Callable
from sqlalchemy.ext.asyncio import AsyncSession
from house_calendar.db.session import engine, async_session
from house_calendar.db.table_models import Base
from fastapi import FastAPI


@pytest.fixture
def mock_session():
    class MockSession:
        def add(self, obj):
            pass

        def commit(self, *args):
            pass

    return MockSession()


@pytest_asyncio.fixture(scope="session")
async def db_engine() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)  # type: ignore
        await connection.run_sync(Base.metadata.create_all)  # type: ignore
        session = async_session(bind=connection, expire_on_commit=False)
        return session


@pytest_asyncio.fixture(autouse=True)
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

    await session.flush()
    await session.rollback()


@pytest.fixture()
def override_get_db(db_session: AsyncSession) -> Callable:
    async def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def app(override_get_db: Callable) -> FastAPI:  # type: ignore
    from house_calendar.db import get_db
    from house_calendar.api import app  # type: ignore

    app.dependency_overrides[get_db] = override_get_db  # type: ignore
    return app  # type: ignore
