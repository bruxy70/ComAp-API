import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
logging.basicConfig(level=logging.ERROR)

values = comapapi(KEY,TOKEN).values(GENSET_ID)
print('Genset values')
print('-------------------------------------------')
for value in values:
    print(f'{value["valueGuid"]} {value["name"]:<24} : {value["value"]} {value["unit"]}')
