from library.mobile.drivers import get_driver


def driver():
    return get_driver()


def go_back():
    driver().back()