import pytest
from house_calendar import config

def test_config_db_config():
    assert isinstance(config.DB_CONFIG.ENGINE_URI, str)
    assert "postgres" in config.DB_CONFIG.ENGINE_URI
    assert "5432" in config.DB_CONFIG.ENGINE_URI