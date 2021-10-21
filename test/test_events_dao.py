from house_calendar.routers.events_dao import add_event_dao, delete_event_dao


def test_add_event_dao(caplog, event_dao_fixture, mock_session):
    test_session = mock_session
    test_event = event_dao_fixture
    result = add_event_dao(test_event, test_session)
    assert type(result) is dict