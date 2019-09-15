import logging
from config import KEY, TOKEN
from comap.api import comapapi
logging.basicConfig(level=logging.DEBUG)

units = comapapi(KEY,TOKEN).units()
print('List of units available within user account')
print('-------------------------------------------')
for unit in units:
    print(f'{unit["unitGuid"]} : {unit["name"]}')
