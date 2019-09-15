import logging
from config import KEY, TOKEN, GENSET_ID
from comap.api import comapapi
logging.basicConfig(level=logging.ERROR)

comments = comapapi(KEY,TOKEN).comments(GENSET_ID)
print('Comments')
for comment in comments:
    print(f'{comment["auhtor"]:<18} {comment["date"]} {comment["text"]}')
