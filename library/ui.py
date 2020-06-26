from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library.configs import IS_ANDROID
from library.drivers import get_appium_driver

LONG_WAIT = 10
SHORT_WAIT = 3


class Element:
    selector = ()
    context: webdriver.Remote = None
    waiter = None
    wait_time: int = SHORT_WAIT

    def __init__(self, android_by: tuple = (), ios_by: tuple = (), long_wait=False):
        self.wait_time = LONG_WAIT if long_wait else SHORT_WAIT
        if IS_ANDROID:
            self.selector = android_by
        else:
            self.selector = ios_by

    def __get__(self, instance, owner):
        self.context = instance.driver
        print('ada di __GET__')
        print('context:', self.context)
        return self._search_element()

    def __getattribute__(self, item):
        if hasattr(Element, item):
            print('masuk kondisional di __GETATTRIBUTE', item)
            return object.__getattribute__(self, item)
        print('Dalemannya __GETATTRIBUTE', item)
        return self._search_element().__getattribute__(item)

    def __getitem__(self, item):
        print('Dalemannya __getitem__', item)
        el = self._search_element()
        print('el:', el)
        return el.__getitem__(item)

    def _search_element(self) -> WebElement:
        if not self.context:
            # if instance has no driver, fill it with current driver
            self.context = get_appium_driver()

        if not self.waiter:
            self.waiter = WebDriverWait(self.context, self.wait_time)
        print('Searching element: ', self.selector)
        el = self.waiter.until(EC.presence_of_element_located(self.selector))
        el.__class__ = WebElement
        return el


class Elements(Element):
    def _search_element(self) -> list:
        if not self.context:
            # if instance has no driver, fill it with current driver
            self.context = get_appium_driver()

        if not self.waiter:
            self.waiter = WebDriverWait(self.context, self.wait_time)

        return self.waiter.until(EC.presence_of_all_elements_located(self.selector))
