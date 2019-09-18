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
from comap.api_async import wsv_async
from comap.constants import VALUE_GUID
# logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.CRITICAL)

async def check_status():
    session=aiohttp.ClientSession(raise_for_status=True)
    wsv=wsv_async(session,KEY,TOKEN)
    units = await wsv.async_units()
    print(f'{"Name":>35}  {"State":<12} {"Mode":<5} Since')
    print('---------------------------------------------------------------------------')
    for unit in units:
        values=await wsv.async_values(unit["unitGuid"],f'{VALUE_GUID["comm_state"]},{VALUE_GUID["mode"]}')
        if len(values)==2:
            print(f'{unit["name"]:>35}  {values[0]["value"]:<12} {values[1]["value"]:<5} {values[1]["timeStamp"]}')
        else:
            print(f'{unit["name"]:>35}  {values[0]["value"]:<12} N/A')
    await session.close()

asyncio.run(check_status())
