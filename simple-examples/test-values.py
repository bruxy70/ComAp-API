import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
logging.basicConfig(level=logging.ERROR)

VALUE_GUIDS = '6a12aed6-3be0-44c4-9110-9ea33cfe3ccc,'\
              'BB2D1ADE-740E-488d-853B-6BA970D52E27,'\
              '72D0295A-3E65-11DF-892C-D6A856D89593,'\
              'B7E5B9B1-9F5E-45c1-82F4-3A336F1F97FA'
values = comapapi(KEY,TOKEN).values(GENSET_ID,VALUE_GUIDS)
print('Genset values')
print('-------------------------------------------')
for value in values:
    print(f'{value["name"]:<16} : {value["value"]} {value["unit"]}')
