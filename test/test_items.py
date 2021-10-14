import pytest

def test_event_valid(event_valid_fixture):
    test_event = event_valid_fixture
    test_event_dict = test_event.dict()
    assert test_event_dict["duration"].seconds == 18000
