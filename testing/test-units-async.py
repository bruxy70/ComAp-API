import asyncio
import logging
import aiohttp
from datetime import datetime, time
from config import KEY, TOKEN
from comap.api_async import wsv_async

logging.basicConfig(level=logging.ERROR)

async def test():
    session = aiohttp.ClientSession(raise_for_status=True)
    wsv = wsv_async(session, KEY, TOKEN)
    units = await wsv.async_units()
    print('List of units available within user account')
    print('-------------------------------------------')
    for unit in units:
        print(f'{unit["unitGuid"]} : {unit["name"]}')
    await session.close()

asyncio.run(test())
