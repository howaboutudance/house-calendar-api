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

# TODO: make seperate router and build out dao/schemas/tables 
# @app.get("/locations/", tags=["location"])
# async def get_location_list(
#     list_parameters: ListParameters = Depends(ListParameters)) -> JSONResponse:
#     resp = [{
#         **location, # type: ignore
#         "events": [
#             {
#                 "name": event["name"],
#                 "start_date": event["start_date"],
#                 "end_date": event["end_date"],
#                 "id": event["id"]
#             } for event in events_db
#             if event["location"]["name"] == location["name"] # type: ignore
#             ]}
#         for location in locations_db
#     ][list_parameters.offset:list_parameters.limit]
#     return JSONResponse(resp)