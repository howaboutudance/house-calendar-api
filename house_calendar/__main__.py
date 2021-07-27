import uvicorn
import os
if "HOST_SERVER" in os.environ:
    host_ip = os.environ["HOST_SERVER"]
else:
    host_ip = "127.0.0.1"

uvicorn.run("house_calendar.main:app", host=host_ip)