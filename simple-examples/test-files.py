import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
logging.basicConfig(level=logging.ERROR)

files = comapapi(KEY,TOKEN).files(GENSET_ID)
print('Files')
print('-------------------------------------------')
for file in files:
    print(f'{file["generated"]} [{file["fileName"]}]')

