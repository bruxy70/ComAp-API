import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
logging.basicConfig(level=logging.DEBUG)

VALUE_GUID = 'BB2D1ADE-740E-488d-853B-6BA970D52E27'

history = comapapi(KEY,TOKEN).history(GENSET_ID,'09/01/2019','09/13/2019',VALUE_GUID)
print('Engine State history')
print('-------------------------------------------')
for event in history[0]["history"]:
    print(f'{event["value"]:<10} valit to {event["validTo"]}')
