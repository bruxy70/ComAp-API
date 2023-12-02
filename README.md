# ComAp API

Allows easy automation of WebSupervisor tasks, such as downloading and analyzing data. It utilizes the [ComAp-API [package](https://pypi.org/project/comap/), which manages calls to the official ComAp API.

## Setup & Configuration

1. Install Python (3.11 or newer)
2. Download the files from the test directory
3. Get the `ComAp-Key`, `client_id` and `secret` and add them to the `.env.secret` file, together with your WSV user name.

## Documentation

The documentation with examples is available on [this Jupyter notebook](https://nbviewer.jupyter.org/github/bruxy70/ComAp-API/blob/development/Documentation.ipynb), including the instructions to get the `ComAp-Key`, `client_id` and `secret`.

*The ``asyncio`` examples are [also available](https://nbviewer.jupyter.org/github/bruxy70/ComAp-API/blob/development/Asyncio%20test.ipynb)*

## Example Scripts

In the ``examples`` directory, there are examples of useful scripts:

- ``archive_files.py <age>`` will download  the files stored on all units registered on your account. You can call it with a parameter to specify maximum age of files to be downloaded. It will create a directory for each unit that has fles to download.
- The batch file ``7-days-backup`` is simply calling ``python archive_files.py 7`` - you can just double-click on it.
- ``check_mode.py`` is listing communication state and mode of the controllers registered under your account. This can be further customized to for example identify units that are not in ``AUT`` mode and make further actions (e.g. send notification).

## Testing

All the examples included in the Jupyter notebook are alao available in the ``testing`` directory. You can run them with your account and play with them.
