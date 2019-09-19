import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import wsv
logging.basicConfig(level=logging.ERROR)

files = wsv(KEY,TOKEN).files(GENSET_ID)
print('Files')
print('-------------------------------------------')
for file in files:
    print(f'{file["generated"]} [{file["fileName"]}]')

