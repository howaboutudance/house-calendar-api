from typing import Text
from datetime import datetime

def incrementable_id():
    id = 0
    def increment() -> int:
        nonlocal id
        id += 1
        return id
    return increment

def create_iso_date(*args: ...) -> Text:
    return datetime(*args).isoformat()

inc_location_id = incrementable_id()
inc_event_id = incrementable_id()
inc_promotors_id = incrementable_id()

orient_express = {"name": "Orient Express", 
"address": "2963 4th Ave S, Seattle, WA 98134", "id": inc_location_id()}
monkey_loft = {"name": "Monkey Loft",
"address": "2915 1st Ave S, Seattle, WA 98134", "id": inc_location_id()}

locations_db = [orient_express, monkey_loft]
soft_option_description = """Join us as we Relaunch Soft Option this Saturday July 3rd at Monkey Loft
10pm-4am
DJs
Karl Kamakahi, Robby Clark, Julie Herrera B2B Trinitron (J/Tron), Mister Smith, and Frank James!!
Here's is the link >>>
https://www.eventbrite.com/.../soft-option-tickets...
So far expected protocol at Monkey will be no mask if you vaccinated while outside, but masks must be worn inside until further notice.
We will update this page as covid restrictions change! June 30th is the scheduled date!
If you have any questions or concerns please email us at delacreme@gmail.com or direct message Karl Kamakahi
Thank You for your love and support,
Big Love from De La Crème Crew !!
See you all on the floor July 3rd ❤"""

events_db = [
    {"name": "Train Car House Party", "id": inc_event_id(), 
    "start_date": datetime(2021, 6, 26, 21).isoformat(),
    "end_date": datetime(2021, 6, 27, 4).isoformat(), "location": orient_express},
    {"name": "Soft Option", "id": inc_event_id(), 
    "start_date": create_iso_date(2021, 7, 3, 21),
    "end_date": create_iso_date(2021, 7, 4, 4), "location": monkey_loft,
    "description": soft_option_description,
    "tickets_url": "https://www.eventbrite.com/e/soft-option-relaunch-july-3rd-tickets-159557497771"
    },
    {"name":"Habitat", "id": inc_event_id(), 
    "start_date": create_iso_date(2021, 7, 14, 21),
    "end_date": create_iso_date(2021, 7, 15, 4), "location": monkey_loft},
    {"name": "Lost", "id": inc_event_id(),
    "start_date": create_iso_date(2021, 7, 10, 22),
    "end_date": create_iso_date(2021, 7, 11, 4), "location": monkey_loft}
]