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

import setuptools
from house_calendar import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="house_calendar_api", # Replace with your own username
    version=__version__,
    author="Micahel Penhallegon",
    author_email="mike@hematite.tech",
    description="A simple api to handle adding, retrieving and managing house music events",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mpenhall-celgene/dc-fast-example",
    project_urls={
        "Bug Tracker": "https://github.com/mpenhall-celgene/dc-fast-example/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "asyncpg",
        "alembic",
        "psycopg2-binary"
    ],
    python_requires='>=3.6',
)