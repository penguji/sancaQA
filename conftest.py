import os

import pytest
from applitools.common import MatchLevel
from applitools.selenium import Eyes

from library.mobile import configs
from library.mobile.drivers import get_driver, quit_driver


@pytest.fixture()
def driver():
    driver = get_driver()
    driver.implicitly_wait(10)
    yield driver
    quit_driver()


@pytest.fixture()
def eyes(request):
    eyes = Eyes()
    if os.environ.get("APPLITOOLS_API_KEY") is not None:
        eyes.api_key = os.getenv("APPLITOOLS_API_KEY")
        eyes.open(get_driver(), app_name=configs.APP_NAME, test_name=request.node.name)
    yield eyes
    eyes.abort()


def validate_screen(eye, tags=None):
    eye.match_level = MatchLevel.STRICT
    eye.check_window(tag=tags)
