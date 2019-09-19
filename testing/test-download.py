import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import wsv
logging.basicConfig(level=logging.ERROR)

# Please run the script test-files, pick a file name and fill it in here
FILENAME = '2019-04-02_13-59_IL3 AMF25 - nahradnik - GSM.csv'

print(f'Downloading file {FILENAME}')
downloaded=wsv(KEY,TOKEN).download(GENSET_ID,FILENAME)
print(f"{FILENAME} download {'SUCCESS' if downloaded else 'FAILED'}")    