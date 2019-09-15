"""
From all controllers registered under the user account, archive the files yanger than given days (will create a directory for each controller)
To run: python archive_files.py
"""
import logging
import os
import asyncio
import logging
import aiohttp
from config import KEY, TOKEN
from datetime import datetime,date
from comap.api_async import comapapi_async
logging.basicConfig(level=logging.ERROR)

async def backup():
    session=aiohttp.ClientSession(raise_for_status=True)
    wsv=comapapi_async(session,KEY,TOKEN)
    units = await wsv.async_units()
    for unit in units:
        files=await wsv.async_files(unit["unitGuid"])
        print(f'Archiving {unit["name"]}...')    
        for file in list(filter(lambda f: (today-datetime.strptime(f["generated"],"%Y-%m-%d %H:%M:%SZ").date()).days<=age,files)):
            print(f'Downloading file {file["fileName"]}')
            if not os.path.exists(unit["name"]): os.mkdir(unit["name"])
            downloaded=await wsv.async_download(unit["unitGuid"],file["fileName"],unit["name"])
            print(f"{'SUCCESS' if downloaded else 'FAILED'}")
    await session.close()

today=datetime.now().date()
try:
    age=int(input("Enter maximum age of the files to download (in days): "))
except ValueError as e:
    print("The age must be a number!")        
    quit()

asyncio.run(backup())
