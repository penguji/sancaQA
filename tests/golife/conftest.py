from time import sleep

import pytest

from library import adb, configs
from library.drivers import get_appium_driver, close_appium_driver


TEST_COUNT = 0


@pytest.fixture(autouse=True, scope='module')
def hook_module_test_golife():
    driver = get_appium_driver()
    driver.implicitly_wait(5)
    yield driver
    global TEST_COUNT
    TEST_COUNT = 0  # reset counter for hook_each_test
    close_appium_driver()


@pytest.fixture(autouse=True)
def hook_each_test_golife():
    driver = get_appium_driver()
    global TEST_COUNT
    TEST_COUNT += 1
    if configs.IS_ANDROID:
        activity = driver.current_activity
        if 'com.gojek.golife' in activity and TEST_COUNT > 1:
            adb.close_app()
            sleep(1)
            adb.relaunch_app()