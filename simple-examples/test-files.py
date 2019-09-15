import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
from datetime import datetime,datetime

logging.basicConfig(level=logging.DEBUG)

files = comapapi(KEY,TOKEN).files(GENSET_ID)
print('Files')
print('-------------------------------------------')
for file in files:
    print(f'{datetime.strptime(file["generated"],"%Y-%m-%d %H:%M:%SZ").date()}   {file["fileName"]} ')

