# ComAp API
Allows easy automation of WebSupervisor tasks, such as downloading and analyzing data. It utilizes the [ComAp-API package](https://pypi.org/project/comap/), that manages calls to the official ComAp API.

## Setup & Configuration
1. Install Python
2. Download the files from the test directory
3. From your ComAp API Developer portal go to your [Profile](https://portal.websupervisor.net/developer) and copy your  Primary or Secondary Key. 
4. Configure your account - run ``setup.bat`` and follow the instructions! It will generate configuration file ``config.py`` with your API secrets.
5. Copy the ``config.py`` to the `examples` and `simple-examples` directories.

## Documentation
The documentation with examples is available on [this Jupyter notebook](https://nbviewer.jupyter.org/github/bruxy70/ComAp-API/blob/development/Documentation.ipynb)

## Example Scripts
In the ``examples`` directory, there are examples of usefull scripts:
- ``archive_files.py <age>`` will download  the files stored on all units registered on your account. You can call it with a parameter to specify maximum age of files to be downloaded. It will create a directory for each unit that has fles to download.
- The batch file ``7-days-backup`` is simply calling ``python archive_files.py 7`` - you can just double-click on it.
- ``check_mode.py`` is listing communication state and mode of the controllers registered under your account. This can be further customized to for example identify units that are not in ``AUT`` mode and make further actions (e.g. send notification).

## Testing
All the examples included in the Jupyter notebook are alao available in the ``simple-examples`` directory. You can run them with your account and play with them.
