import time

from conftest import validate_screen
from library import adb
from library.drivers import get_appium_driver, close_appium_driver


def test_login(driver, eyes):
    print("login")
    time.sleep(3)
    driver.find_element_by_id("btn_login").click()
    validate_screen(eyes, "login")
    print("device_id", adb.get_device_id())
    print("ip: ", adb.get_android_ip())
    print("model: ", adb.get_android_model())
    print("version: ", adb.get_android_version())
    print("state: ", adb.get_device_state())
    print("sdk: ", adb.get_sdk_version())
    time.sleep(2)