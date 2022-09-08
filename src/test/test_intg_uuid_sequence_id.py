import pytest
from sqlalchemy.ext.asyncio import AsyncSession


pytestmark = pytest.mark.integration


@pytest.mark.skip
@pytest.mark.asyncio
async def test_uuid_sequence_autofill(db_session: AsyncSession):
    add_event_query = """
    INSERT INTO event (name, start_date, end_date, duration, location) 
        VALUES (
            'test event', 
            timestamp with time zone '2022-09-08 20:00:00-08', 
            timestamp with time zone '2022-09-08 20:30:00-08', 
            0, 
            json_object('{name, location}', '{test location, 123 test street}')) 
    """

    try:
        await db_session.execute(add_event_query)
        result = await db_session.execute(
            "SELECT * FROM event WHERE name = 'test event'"
        )
        assert 1 == len(result)
    except:
        assert False
