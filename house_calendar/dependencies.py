from typing import Optional, Text
from fastapi.param_functions import Query

class ListParameters:
    def __init__(self, q: Optional[Text] = Query(None), offset: int = 0, 
        limit: int = 1000):
        self.q = q, 
        self.offset = offset
        self.limit =  offset + limit