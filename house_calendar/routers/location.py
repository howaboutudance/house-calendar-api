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