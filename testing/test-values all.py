"""Demonstration of the ComAp API library

The ComAp Cloud authentication needs client_id and secret. The WSV API need
the user name. These are stored in the `.env.secret` file - you need to add it there.

For the communication with the genset, we also use a genset id (guid).
This one is stored in the .env.shared file - you need to add your controller there as well.

This example lists all the controller unit values - usefull to get value guids.
"""
import logging

from comap import api
from dotenv import dotenv_values

# Retrieve secrets and common values stored in the .env files
secrets = dotenv_values(".env.secret")
shared = dotenv_values(".env.shared")

logging.basicConfig(level=logging.ERROR)

# Use the ComAp Cloud Identity API to get the Bearer token
identity = api.Identity(secrets["COMAP_KEY"])
token = identity.authenticate(secrets["CLIENT_ID"], secrets["SECRET"])

if token is not None:
    # Create WSV instance to call APIs
    wsv = api.WSV(secrets["LOGIN_ID"], secrets["COMAP_KEY"], token["access_token"])
    values = wsv.values(shared["GENSET_ID"])
    print('Genset values')
    print('-------------------------------------------')
    for value in values:
        print(f'{value["valueGuid"]} {value["name"]:<24} : {value["value"]} {value["unit"]}')
