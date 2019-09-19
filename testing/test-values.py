import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import wsv
from comap.constants import VALUE_GUID

logging.basicConfig(level=logging.ERROR)

values = wsv(KEY,TOKEN).values(GENSET_ID,f'{VALUE_GUID["mode"]},{VALUE_GUID["engine_state"]},{VALUE_GUID["nominal_power"]}')
print('Genset values')
print('-------------------------------------------')
for value in values:
    print(f'{value["name"]:<16} : {value["value"]} {value["unit"]}')
