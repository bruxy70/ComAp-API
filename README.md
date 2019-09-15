# ComAp API
Allows easy automation of WebSupervisor tasks, such as downloading and analyzing data

## Setup
1. Download the files from the test directory
2. Install ComAp API package by following command
```
Install python -m pip install --upgrade comap
```
(or run setup.bat)

## Configuration
1. From your ComAp API Developer portal go to your [Profile](https://portal.websupervisor.net/developer) and copy your  Primary or Secondary Key. 
2. Open ``config.py`` file and paste the key in the ``KEY`` string.
3. Run ``python get-token.py``, Enter your WSV user name and password. It will generate Token - copy it.
4. Paste the token in the ``TOKEN`` string of ``config.py``
5. Now copy the ``config.py`` to each test directory

## Testing

