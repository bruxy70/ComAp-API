"""Demonstration of the ComAp Asynchronous API library

The ComAp Cloud authentication needs client_id and secret. The WSV API need
the user name. These are stored in the `.env.secret` file - you need to add it there.

This example lists the controller units configured for the WebSupervisor account.
It is an asynchronous version of the example `test-units`
"""

import asyncio
import logging

import aiohttp
from comap import api_async
from dotenv import dotenv_values

# Retrieve secrets stored in the .env files
secrets = dotenv_values(".env.secret")

logging.basicConfig(level=logging.ERROR)


async def main() -> None:
    """The module runs the test asynchronously, so it uses this async function"""

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
            print("List of units available within user account")
            print("-------------------------------------------")
            for unit in units:
                print(f'{unit["unitGuid"]} : {unit["name"]}')


asyncio.run(main())
