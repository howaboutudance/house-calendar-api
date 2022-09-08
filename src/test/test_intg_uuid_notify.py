import pytest
from house_calendar_events.config import settings
from psycopg2 import connect

pytestmark = pytest.mark.integration


@pytest.mark.asyncio
def test_psycopg2_notify():

    conn = connect(settings.psycopg2_uri)
    cursor = conn.cursor()
    cursor.execute("LISTEN test_feed;")
    cursor.execute("NOTIFY test_feed, 'test';")
    conn.poll()
    for notify in conn.notifies:
        if notify.channel == "test_feed":
            assert "test" == notify.payload

    conn.notifies.clear()


@pytest.mark.asyncio
async def test_add_new_event_notify():
    add_event_event_query = """
    INSERT INTO event (id, name, start_date, end_date, duration, location) 
        VALUES (
            gen_random_uuid(),
            'test event', 
            timestamp with time zone '2022-09-08 20:00:00-08', 
            timestamp with time zone '2022-09-08 20:30:00-08', 
            0, 
            json_object('{name, location}', '{test location, 123 test street}')); 
    """

    conn = connect(settings.psycopg2_uri)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("LISTEN event_id_feed;")
    cursor.execute(add_event_event_query)
    add_event_result = cursor.execute("SELECT * FROM event;")
    popped = None
    cc = 255
    while 0 < cc:
        conn.poll()
        try:
            res = conn.notifies.pop()
            popped = res
        except IndexError:
            cc -= 1
        except UnboundLocalError:
            continue

    cursor.execute("TRUNCATE event;")
    assert popped
    assert popped.channel == "event_id_feed"
    conn.notifies.clear()

    assert 0 < len(add_event_result) < 2
