import time

from conftest import validate_screen
from library import adb
from screens import login
from screens.login_screen import Login


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


def test_page_object_style(driver):
    print("login")
    time.sleep(3)
    # driver.find_element_by_id("btn_login").click()
    login_screen = Login()
    login_screen.btn_login.click()
    time.sleep(2)
    login_screen.go_back()
    login_screen.btn_signup.click()
    time.sleep(2)
    login_screen.driver.back()
    time.sleep(2)
    login_screen.ambil_text()
    time.sleep(2)


def test_module_style(driver):
    time.sleep(3)
    print("Text: ", login.BTN_LOGIN.text)
    login.BTN_LOGIN.click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    login.BTN_SIGNUP.click()
    driver.back()
    for txt in login.TXT_ALL:
        print(txt.text)