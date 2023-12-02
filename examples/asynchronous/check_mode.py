"""
Check the status of all controllers registered in the user account.
This can be used for example to launch automated action if the mode is different than "auto"
"""
import asyncio
import logging

import aiohttp
from comap import api_async
from comap.constants import VALUE_GUID
from dotenv import dotenv_values

# Retrieve secrets and common values stored in the .env files
secrets = dotenv_values(".env.secret")
shared = dotenv_values(".env.shared")

logging.basicConfig(level=logging.CRITICAL)

async def check_status():
    # The aiohttp uses a session https connection pool handler
    async with aiohttp.ClientSession() as session:
        # Use the ComAp Cloud Identity API to get the Bearer token
        identity = api_async.Identity(session, secrets["COMAP_KEY"])
        token = await identity.authenticate(
            secrets["CLIENT_ID"], secrets["SECRET"]
        )

        if token is not None:
            # Create WSV instance to call APIs
            wsv = api_async.WSV(
                session,
                secrets["LOGIN_ID"],
                secrets["COMAP_KEY"],
                token["access_token"],
            )
            units = await wsv.units()
            print(f'{"Name":>35}  {"State":<12} {"Mode":<5} Since')
            print('---------------------------------------------------------------------------')
            for unit in units:
                values = await wsv.values(unit["unitGuid"],f'{VALUE_GUID["comm_state"]},{VALUE_GUID["mode"]}')
                if len(values) == 2:
                    print(f'{unit["name"]:>35}  {values[0]["value"]:<12} {values[1]["value"]:<5} {values[1]["timeStamp"]}')
                elif len(values) > 0:
                    print(f'{unit["name"]:>35}  {values[0]["value"]:<12} N/A')

asyncio.run(check_status())
