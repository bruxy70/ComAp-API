"""
From all controllers registered under the user account, archive the files yanger than given days (will create a directory for each controller)
To run: python archive_files.py <age> (e.g. 'python archive_files.py 7' for the backup of last 7 days)
Age is a number of days and is optional. If no age is given, the script will prompt
"""
import logging
import os
import sys
import logging
from config import KEY, TOKEN
from datetime import datetime, date
import comap.api
logging.basicConfig(level=logging.ERROR)

def backup(age):
    wsv = comap.api.wsv(KEY, TOKEN)
    units = wsv.units()
    for unit in units:
        files = wsv.files(unit["unitGuid"])
        print(f'Archiving {unit["name"]}...')    
        for file in list(filter(lambda f: (today - f["generated"].date()).days <= age, files)):
            print(f'Downloading file {file["fileName"]}')
            if not os.path.exists(unit["name"]):
                os.mkdir(unit["name"])
            downloaded = wsv.download(unit["unitGuid"], file["fileName"], unit["name"])
            print(f"{' - SUCCESS' if downloaded else ' - FAILED'}")

today = datetime.now().date()
try:
    if len(sys.argv) > 1:
        age = int(sys.argv[1])
    else:
        age = int(input("Enter maximum age of the files to download (in days): "))
except ValueError as e:
    print("The age must be a number!")
    quit()

backup(age)
