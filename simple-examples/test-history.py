import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
import timestring
logging.basicConfig(level=logging.ERROR)

VALUE_GUID = 'BB2D1ADE-740E-488d-853B-6BA970D52E27'

history = comapapi(KEY,TOKEN).history(GENSET_ID,'09/10/2019','09/13/2019',VALUE_GUID)
print('Engine State history')
print('-------------------------------------------')
for event in history[0]["history"]:
    print(f'{event["value"]:<8} valit to {event["validTo"]}')
