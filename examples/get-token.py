from comap.api import comapapi
import getpass 

print('This program will generate a configuration file, that will store your credentials to use ComAp API.\n')
print('You will need ComAp API, that you will find on the ComAp API developer portal under your profile.')
print('Then you will need your WebSupervisor user name and password.')
print('It will generate your security token and store it, together wit the key, in the config.py file.\n')
proceed=str(input('Do you want to continue? (Yes/No)')).lower().strip()[0]
if proceed=='y':
    print('\nFirst, go to your ComAp API profile (https://portal.websupervisor.net/developer) and get your Primary and Secondary Key.')
    comap_key= input("Enter your key (one of them): ")
    username = input("Enter your WebSupervisor user name: ")
    password = getpass.getpass("Enter your WebSupervisor password: ")
    token = comapapi(comap_key,'').authenticate(username,password)
    if token!=None:
        f = open("config.py", "w")
        f.write(f"KEY='{comap_key}'\n")
        f.write(f"TOKEN='{token}'")
        f.close()
        print('\nThe KEY and TOKEN are stored in the config.py file. Copy this file to the directories with examples.\n')
        print('KEEP THIS FILE SECRET! Do not share it with anyone, do not post it on Internet!\nIt contains the information used to authenticate to ComAp API with your user account.\n')
        print('If your keys get compromised, generate a new KEY on the WebSupervisor portal!\nThe KEY will automatically become invalid if not used for 30 days!\n')
    else:
        print('That did not work!\n')