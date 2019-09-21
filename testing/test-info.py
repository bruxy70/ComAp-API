import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import wsv
logging.basicConfig(level=logging.ERROR)

info = wsv(KEY, TOKEN).info(GENSET_ID)
print('Information')
print('-------------------------------------------')
print(f'Name:        {info["name"]}')
print(f'Owner:       {info["ownerLoginId"]}')
print(f'Application: {info["applicationType"]}')
print(f'Timezone:    {info["timezone"]}')
print(f'Airgate ID:  {info["connection"]["airGateId"]}')
print(f'Position:    {info["position"]["latitude"]},{info["position"]["longitude"]}')
