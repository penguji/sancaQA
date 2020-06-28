import os
from dotenv import load_dotenv
from library.devices import android_udid, wda_port

load_dotenv()

APPIUM_TIMEOUT = 300
APPIUM_SERVER = os.getenv("APPIUM_SERVER")
PLATFORM = os.getenv("TEST_PLATFORM", "android").lower()
APP_NAME = os.getenv("TEST_APP_NAME")
APP_ANDROID_ACTIVITY = os.getenv("TEST_APP_ANDROID_ACTIVITY")
IS_ANDROID = PLATFORM.upper() == "ANDROID"
IS_IOS = PLATFORM.upper() == "IOS"
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_TIMEOUT", "3"))

CAPABILITIES = {
    "android": {
        "platformName": "Android",
        "deviceName": "Android",
        "appPackage": APP_NAME,
        "appActivity": APP_ANDROID_ACTIVITY,
        "automationName": "UiAutomator2",
        "newCommandTimeout": APPIUM_TIMEOUT,
        "noReset": True,
        "autoGrantPermissions": True,
        "udid": android_udid(),
    },
    "ios": {
        "version": "",
        "platformName": "",
        "platformVersion": "",
        "deviceName": "",
        "app": "",
        "noReset": "",
        "fullReset": "",
        "newCommandTimeout": "",
        "wdaLocalPort": wda_port(),
    },
}.get(PLATFORM)
