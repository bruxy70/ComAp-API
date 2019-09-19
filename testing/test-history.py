import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import wsv
from comap.constants import VALUE_GUID
import timestring
logging.basicConfig(level=logging.ERROR)

VALUE_GUID = VALUE_GUID['engine_state']

history = wsv(KEY,TOKEN).history(GENSET_ID,'09/10/2019','09/13/2019',VALUE_GUID)
print('Engine State history')
print('-------------------------------------------')
for event in history[0]["history"]:
    print(f'{event["value"]:<8} valit to {event["validTo"]}')
