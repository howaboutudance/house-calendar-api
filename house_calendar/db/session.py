from house_calendar.db.tables_models import Base
from ..config import DB_CONFIG
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(DB_CONFIG.ENGINE_URI, future=True, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, 
        expire_on_commit=False)


# async def init_db():
#     async with engine.begin as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
# 
# 
# async def get_session() -> AsyncSession:
#     async with async_session as session:
#         yield session
#         await session.commit()

async def get_db() -> AsyncSession:
    """
    Dependency function that yields db sessions
    """
    async with async_session() as session:
        yield session
        await session.commit()