import os

import pytest
from applitools.selenium import Eyes

from library.drivers import get_appium_driver, close_appium_driver


@pytest.fixture()
def driver():
    driver = get_appium_driver()
    driver.implicitly_wait(10)
    yield driver
    close_appium_driver()


@pytest.fixture()
def eyes(request):
    eyes = Eyes()
    if os.environ.get("APPLITOOLS_API_KEY") is not None:
        print("Keynya: ", os.environ.get("APPLITOOLS_API_KEY"))
        eyes.api_key = os.environ.get("APPLITOOLS_API_KEY")
        eyes.open(driver, app_name="Golife", test_name=request.node.name)
    yield eyes
    eyes.abort()
