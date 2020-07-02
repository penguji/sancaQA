import pytest

from library.mobile import configs
from library.mobile.devices import get_device_id
from library.mobile.drivers import quit_driver, create_appium_session

GOLIFE_CAPS = None


@pytest.fixture(autouse=True, scope='module')
def hook_module_test_golife(request):
    print("=== Before All ===")
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
    driver = create_appium_session(get_device_id(), GOLIFE_CAPS)
    print("=== Before Test ===")

    def tear_down():
        print("=== After Test ===")
        quit_driver()
    request.addfinalizer(tear_down)