from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from typing import AsyncGenerator

from ..config import DB_CONFIG

engine = create_async_engine(DB_CONFIG.ENGINE_URI, future=True, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, 
        expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency function that yields db sessions
    """
    async with async_session() as session:
        yield session
        await session.commit()