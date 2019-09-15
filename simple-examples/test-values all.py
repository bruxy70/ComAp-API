import logging
from config import KEY, TOKEN
from comap.api import comapapi
logging.basicConfig(level=logging.ERROR)

GENSET_ID = 'genseted7885ae364e407ca372a12155d0dea5'

values = comapapi(KEY,TOKEN).values(GENSET_ID)
print('Genset values')
print('-------------------------------------------')
for value in values:
    print(f'{value["valueGuid"]} {value["name"]:<24} : {value["value"]} {value["unit"]}')
