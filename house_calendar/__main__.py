import uvicorn
import os
if "HOST_SERVER" in os.environ and "HOST_PORT" in os.environ:
    host_ip = os.environ["HOST_SERVER"]
    host_port = int(os.environ["HOST_PORT"])
else:
    host_ip = "127.0.0.1"
    host_port = 8000

uvicorn.run("house_calendar.api:app", host=host_ip, port=host_port)