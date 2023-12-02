"""
Check the status of all controllers registered in the user account.
This can be used for example to launch automated action if the mode is different than "auto"
"""
import logging

from comap import api, constants
from dotenv import dotenv_values

# Retrieve secrets and common values stored in the .env files
secrets = dotenv_values(".env.secret")
shared = dotenv_values(".env.shared")

logging.basicConfig(level=logging.CRITICAL)

def check_status():
    # Use the ComAp Cloud Identity API to get the Bearer token
    identity = api.Identity(secrets["COMAP_KEY"])
    token = identity.authenticate(secrets["CLIENT_ID"], secrets["SECRET"])

    if token is not None:
        # Create WSV instance to call APIs
        wsv = api.WSV(secrets["LOGIN_ID"], secrets["COMAP_KEY"], token["access_token"])
        units = wsv.units()
        print(f'{"Name":>35}  {"State":<12} {"Mode":<5} Since')
        print('---------------------------------------------------------------------------')
        for unit in units:
            values = wsv.values(unit["unitGuid"],f'{constants.VALUE_GUID["comm_state"]},{constants.VALUE_GUID["mode"]}')
            if len(values) == 2:
                print(f'{unit["name"]:>35}  {values[0]["value"]:<12} {values[1]["value"]:<5} {values[1]["timeStamp"]}')
            elif len(values) > 0:
                print(f'{unit["name"]:>35}  {values[0]["value"]:<12} N/A')

check_status()
