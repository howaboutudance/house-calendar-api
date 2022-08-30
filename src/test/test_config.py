# Copyright 2021-2022 Michael Penhallegon
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
from house_calendar_events import config
from dynaconf import base


def test_dynaconf_settings():
    assert isinstance(config.settings, base.LazySettings)


def test_dynaconf_setting_var():
    assert "test_var" == config.settings.test_var


def test_postgres_uri_var_exists():
    assert "POSTGRES_URI" in config.settings
    assert str(config.settings.postgres_uri).startswith("postgresql+asyncpg://")


def test_origins_var_exists():
    assert "ORIGINS" in config.settings
    assert isinstance(config.settings.origins, list)
    assert all(
        [
            (url.startswith("http://") or url.startswith("https://"))
            for url in config.settings.origins
        ]
    )


def test_alembic_uri_formatted():
    expected = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/hc_events"
    assert "ALEMBIC_URI" in config.settings
    assert expected == config.settings.alembic_uri
