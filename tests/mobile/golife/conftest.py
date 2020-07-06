import pytest

from library.mobile import configs
from library.mobile.configs import LOGGER
from library.mobile.devices import get_device_id
from library.mobile.drivers import create_appium_session, quit_driver

GOLIFE_CAPS = None


@pytest.fixture(autouse=True, scope="module")
def hook_module_test_golife(request):
    LOGGER.info("=== Before All ===")
    global GOLIFE_CAPS
    GOLIFE_CAPS = configs.load_caps(configs.PLATFORM, "caps_golife.json")

    # Can happen:
    # - Modify caps
    # - Install app
    # - Reset setting
    # - Do login

    def tear_down():
        print("=== After All ===")
        # Delete App

    request.addfinalizer(tear_down)


@pytest.fixture(autouse=True)
def hook_each_test_golife(request):
    global GOLIFE_CAPS
    create_appium_session(get_device_id(), GOLIFE_CAPS)
    LOGGER.info(f"=== Before Test '{request.node.name}' ===")

    def tear_down():
        LOGGER.info(f"=== After Test '{request.node.name}' ===")
        quit_driver()

    request.addfinalizer(tear_down)
