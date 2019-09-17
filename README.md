# ComAp API
Allows easy automation of WebSupervisor tasks, such as downloading and analyzing data

## Setup
1. Install Python
2. Download the files from the test directory
3. Install ComAp API package by following command
```
setup.bat
```
(or simply ``python -m pip install --upgrade comap``)

## Configuration
1. From your ComAp API Developer portal go to your [Profile](https://portal.websupervisor.net/developer) and copy your  Primary or Secondary Key. 
2. From your command line, execute ``python get-token.py``. Follow the instructions! It will generate configuration file ``config.py`` with your API secrets.
3. Copy the ``config.py`` to each test directory

## Testing
In the ``simple-examples`` directory, there are examples of individual functions
In the ``examples`` directory, there are examples of already usefull scripts, that are combining multiple functions:
- ``archive_files.py <age>`` will download  the files stored on all units registered on your account. You can call it with a parameter to specify maximum age of files to be downloaded. It will create a directory for each unit that has fles to download.
- The batch file ``7-days-backup`` is simply calling ``python archive_files.py 7`` - you can just double-click on it.
- ``check_mode.py`` is listing communication state and mode of the controllers registered under your account. This can be further customized to for example identify units that are not in ``AUT`` mode and make further actions (e.g. send notification).
