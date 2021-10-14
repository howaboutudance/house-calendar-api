from typing import Union, List, Dict, Text
## Tyoe Definitions
JSONSingleton = Union[Text, int, float, bool]
JSONType = Union[JSONSingleton, List['JSONType'], Dict[Text, 'JSONType']] # type: ignore