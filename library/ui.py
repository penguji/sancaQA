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
    wait = None

    def __init__(self, android_by: tuple = (), ios_by: tuple = (), short_wait = False):
        self.wait_time = SHORT_WAIT if short_wait else LONG_WAIT
        if IS_ANDROID:
            self.selector = android_by
        else:
            self.selector = ios_by

    def __get__(self, instance, owner):
        self.context = instance.driver
        if not self.context:
            self.context = get_appium_driver()
        return self._search_element()

    def _search_element(self) -> WebElement:
        if not self.context:
            raise Exception("Search context should be defined with dynamic Find usage")

        if not self.wait:
            self.wait = WebDriverWait(self.context, self.wait_time)

        el = self.wait.until(EC.presence_of_element_located(self.selector))
        el.__class__ = WebElement
        return el


class Elements(Element):
    def _search_element(self) -> list:
        if not self.wait:
            self.wait = WebDriverWait(self.context, self.wait_time)

        return self.wait.until(EC.presence_of_all_elements_located(self.selector))
