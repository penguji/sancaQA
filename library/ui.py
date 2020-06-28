from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from library import configs
from library.configs import IS_ANDROID
from library.drivers import get_appium_driver


class WebElementPatch(WebElement):
    def find_text(self, text: str, case_sensitive=True):
        selector_strict = {
            "android": f"//android.widget.TextView[@text='{text}']",
            "ios": f"//*[@label='{text}' and @visible='true']"
        }.get(configs.PLATFORM)
        selector_case_insensitive = {
            "android": f"//android.widget.TextView[lower-case(@text)='{text.lower()}']",
            "ios": f"//*[@label='{text.lower()}' and @visible='true']"
        }.get(configs.PLATFORM)

        selector = selector_strict if case_sensitive else selector_case_insensitive
        # Let's assume this method call when UI ready
        # so implicit timeout we set to 0 for make it fast
        get_appium_driver().implicitly_wait(0)
        list_data = self.find_elements(by=By.XPATH, value=selector.format(text))
        # restore back implicit wait
        get_appium_driver().implicitly_wait(configs.IMPLICIT_WAIT)
        return list_data

    def has_text(self, text: str, case_sensitive=True) -> bool:
        data = self.find_text(text, case_sensitive)
        return len(data) > 0

    def has_no_text(self, text: str, case_sensitive=True) -> bool:
        data = self.find_text(text, case_sensitive)
        return len(data) == 0


class Element:
    selector = ()
    context: webdriver.Remote = None
    waiter = None
    wait_time: int = 1

    def __init__(self, android_by: tuple = (), ios_by: tuple = (), wait_time: int = 1):
        self.wait_time = wait_time
        if IS_ANDROID:
            self.selector = android_by
        else:
            self.selector = ios_by

    def __get__(self, instance, owner):
        self.context = instance.driver
        return self._search_element()

    def __getattribute__(self, item):
        if hasattr(Element, item):
            return object.__getattribute__(self, item)
        return self._search_element().__getattribute__(item)

    def __getitem__(self, item):
        el = self._search_element()
        return el.__getitem__(item)

    def _search_element(self) -> WebElementPatch:
        if not self.context:
            # if instance has no driver, fill it with current driver
            self.context = get_appium_driver()

        if not self.waiter:
            self.waiter = WebDriverWait(self.context, self.wait_time)
        el = self.waiter.until(EC.presence_of_element_located(self.selector))
        el.__class__ = WebElementPatch
        return el


class Elements(Element):
    def _search_element(self) -> list:
        if not self.context:
            # if instance has no driver, fill it with current driver
            self.context = get_appium_driver()

        if not self.waiter:
            self.waiter = WebDriverWait(self.context, self.wait_time)

        return self.waiter.until(EC.presence_of_all_elements_located(self.selector))
