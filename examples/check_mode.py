"""
Check the status of all controllers registered in the user account.
This can be used for example to launch automated action if the mode is different than "auto"
"""
import logging
import os
import sys
import asyncio
import logging
import aiohttp
from config import KEY, TOKEN
from datetime import datetime,date
from comap.api_async import comapapi_async
# logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.CRITICAL)

#Tohle bych dal primo do ty knihovny jako konstantu, s par beznejma hodnotama.
VALUE_GUID = {
    "engine_state": "BB2D1ADE-740E-488d-853B-6BA970D52E27",
    "mode":         "6a12aed6-3be0-44c4-9110-9ea33cfe3ccc",
    "state":        "F0219C1C-1860-4b4d-8E6E-3CEC96279D6F",
    "fuel_level":   "0dc2739f-0fc9-4a17-bc91-26e5dda19ed8"
}

async def check_status():
    session=aiohttp.ClientSession(raise_for_status=True)
    wsv=comapapi_async(session,KEY,TOKEN)
    units = await wsv.async_units()
    print(f'{"Name":>35}  {"State":<12} {"Mode":<5} Since')
    print('---------------------------------------------------------------------------')
    for unit in units:
        values=await wsv.async_values(unit["unitGuid"],f'{VALUE_GUID["state"]},{VALUE_GUID["mode"]}')
        # if len(values)>0 and values[0]["value"]=='Online':
        #     print(f'{unit["name"]:>35}  {values[0]["value"]:<12} {values[1]["value"]:<5} {values[1]["timeStamp"]}')
        if len(values)==1:
            print(f'{unit["name"]:>35}  {values[0]["value"]:<12} N/A')
        elif len(values)==2:
            print(f'{unit["name"]:>35}  {values[0]["value"]:<12} {values[1]["value"]:<5} {values[1]["timeStamp"]}')
        else:
            print(f'{unit["name"]:>35}  N/A')
    await session.close()

asyncio.run(check_status())

