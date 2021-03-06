"""
Check the status of all controllers registered in the user account.
This can be used for example to launch automated action if the mode is different than "auto"
"""
import logging
import os
import sys
import logging
from config import KEY, TOKEN
from datetime import datetime, date
import comap.api
from comap.constants import VALUE_GUID
logging.basicConfig(level=logging.CRITICAL)

def check_status():
    wsv = comap.api.wsv(KEY, TOKEN)
    units = wsv.units()
    print(f'{"Name":>35}  {"State":<12} {"Mode":<5} Since')
    print('---------------------------------------------------------------------------')
    for unit in units:
        values = wsv.values(unit["unitGuid"],f'{VALUE_GUID["comm_state"]},{VALUE_GUID["mode"]}')
        if len(values) == 2:
            print(f'{unit["name"]:>35}  {values[0]["value"]:<12} {values[1]["value"]:<5} {values[1]["timeStamp"]}')
        else:
            print(f'{unit["name"]:>35}  {values[0]["value"]:<12} N/A')

check_status()
