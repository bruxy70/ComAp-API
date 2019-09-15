import logging
from config import KEY, TOKEN
from comap.api import comapapi
logging.basicConfig(level=logging.DEBUG)

GENSET_ID = 'genseta3813e5af9fb419293778e95cdfa9e80'

files = comapapi(KEY,TOKEN).files(GENSET_ID)
print('Files')
print('-------------------------------------------')
for file in files:
    print(f'{file["fileName"]}')
