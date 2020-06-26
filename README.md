![python](python.gif)
# SancaQA 🐍
Simplify Mobile Automation Test


## Features
- Easy to write automated test of mobile app
- Support Android and Ios
- Human readable
- Enable Visual testing (soon)


## Setup
- Run command `pipenv install` to install required libraries inside python virtual environment (pipenv)
- Run command `cp .env.sample .env` to create new config, edit the keys with your desired app info
- Spawn appium server by running command `appium` * Note if you spawn with specific port, please update list of appium port at method `get_appium_server()` at `library/drivers.py`
- Run the test by using command `pipenv run pytest tests/pertamax_test.py`

## Additional Stuff
- I recommend to install [scrcpy](https://github.com/Genymobile/scrcpy) to ease monitoring device in computer using mirror device screen share
- To find current activity/package info at android you can use command `adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'`