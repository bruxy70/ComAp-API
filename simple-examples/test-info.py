import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
from datetime import datetime,datetime
logging.basicConfig(level=logging.ERROR)

info = comapapi(KEY,TOKEN).info(GENSET_ID)
print('Information')
print('-------------------------------------------')
print(f'Name:        {info["name"]}')
print(f'Owner:       {info["ownerLoginId"]}')
print(f'Application: {info["applicationType"]}')
print(f'Timezone:    {info["timezone"]}')
print(f'Airgate ID:  {info["connection"]["airGateId"]}')
print(f'Position:    {info["position"]["latitude"]},{info["position"]["longitude"]}')
