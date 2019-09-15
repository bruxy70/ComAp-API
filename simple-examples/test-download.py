import logging
from config import KEY, TOKEN
from comap.api import comapapi
logging.basicConfig(level=logging.DEBUG)

GENSET_ID = 'genseta3813e5af9fb419293778e95cdfa9e80'
FILENAME = '2019-04-02_13-59_IL3 AMF25 - nahradnik - GSM.csv'

print(f'Downloading file {FILENAME}')
downloaded=comapapi(KEY,TOKEN).download(GENSET_ID,FILENAME)
print(f"{FILENAME} download {'SUCCESS' if downloaded else 'FAILED'}")    