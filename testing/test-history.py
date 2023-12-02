"""Demonstration of the ComAp API library

The ComAp Cloud authentication needs client_id and secret. The WSV API need
the user name. These are stored in the `.env.secret` file - you need to add it there.

For the communication with the genset, we also use a genset id (guid).
This one is stored in the .env.shared file - you need to add your controller there as well.

This example lists the engine state history (you need to edit the dates constants below)
"""
import logging

from comap import api, constants
from dotenv import dotenv_values

# Retrieve secrets and common values stored in the .env files
secrets = dotenv_values(".env.secret")
shared = dotenv_values(".env.shared")
VALUE_GUID = constants.VALUE_GUID["engine_state"]
START_DATE = "11/01/2023" # you mignt want to edit this
END_DATE = "11/02/2023"   # you mignt want to edit this

logging.basicConfig(level=logging.ERROR)

# Use the ComAp Cloud Identity API to get the Bearer token
identity = api.Identity(secrets["COMAP_KEY"])
token = identity.authenticate(secrets["CLIENT_ID"], secrets["SECRET"])

if token is not None:
    # Create WSV instance to call APIs
    wsv = api.WSV(secrets["LOGIN_ID"], secrets["COMAP_KEY"], token["access_token"])
    history = wsv.history(shared["GENSET_ID"], START_DATE, END_DATE, VALUE_GUID)
    print("Engine State history")
    print("-------------------------------------------")
    for event in history[0]["history"]:
        print(f'{event["value"]:<8} valit to {event["validTo"]}')
