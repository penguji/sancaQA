from library.drivers import get_appium_driver


class Screens:
    def __init__(self):
        self.driver = get_appium_driver()
