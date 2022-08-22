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

import uvicorn
import os


if "HOST_SERVER" in os.environ and "HOST_PORT" in os.environ:
    host_ip = os.environ["HOST_SERVER"]
    host_port = int(os.environ["HOST_PORT"])
else:
    host_ip = "127.0.0.1"
    host_port = 8000

uvicorn.run("house_calendar.api:app", host=host_ip, port=host_port)