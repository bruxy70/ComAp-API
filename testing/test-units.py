"""Demonstration of the ComAp API library

The ComAp Cloud authentication needs client_id and secret. The WSV API need
the user name. These are stored in the `.env.secret` file - you need to add it there.

This example lists the controller units configured for the WebSupervisor account.
Useful to get the genset ids (guids)
"""
import logging

from comap import api
from dotenv import dotenv_values

# Retrieve secrets stored in the .env files
secrets = dotenv_values(".env.secret")

logging.basicConfig(level=logging.ERROR)

# Use the ComAp Cloud Identity API to get the Bearer token
identity = api.Identity(secrets["COMAP_KEY"])
token = identity.authenticate(secrets["CLIENT_ID"], secrets["SECRET"])

if token is not None:
    # Create WSV instance to call APIs
    wsv = api.WSV(secrets["LOGIN_ID"], secrets["COMAP_KEY"], token["access_token"])
    units = wsv.units()
    print("List of units available within user account")
    print("-------------------------------------------")
    for unit in units:
        print(f'{unit["unitGuid"]} : {unit["name"]}')
