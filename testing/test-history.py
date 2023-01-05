import logging

import timestring
from comap.api import wsv
from comap.constants import VALUE_GUID
from config import GENSET_ID, KEY, TOKEN

logging.basicConfig(level=logging.ERROR)

VALUE_GUID = VALUE_GUID["engine_state"]

history = wsv(KEY, TOKEN).history(GENSET_ID, "12/01/2022", "12/02/2022", VALUE_GUID)
print("Engine State history")
print("-------------------------------------------")
for event in history[0]["history"]:
    print(f'{event["value"]:<8} valit to {event["validTo"]}')
