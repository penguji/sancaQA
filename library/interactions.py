from library.drivers import get_appium_driver


def driver():
    return get_appium_driver()


def go_back():
    driver().back()