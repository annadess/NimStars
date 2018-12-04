# NimStars

Description
------------
Nim Stars is a simple python application. Using the github api, this program gets all public [Nim packages](https://github.com/nim-lang/packages/blob/master/packages.json) and assigns them ratings based on how many stars they got on github. The resulting information is written into the `stars.csv` and `result.csv` files.

Note: Due to github's API limit you'll need to login with your username and password.

How to install & run
--------------------
- Download the source files.
- Make sure you have the `requests` package installed. (`pip install requests`)
- Run `NimStars.py` either directly `./NimStars.py` or through calling python `python NimStars.py`.
