from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library import configs
from library.drivers import get_appium_driver


def wait_for_element(raw_selector):
    def _el():
        wait = WebDriverWait(get_appium_driver(), 10)
        selector = locator_for_platform(raw_selector)
        return wait.until(EC.presence_of_element_located(selector))

    return _el


def wait_for_elements(raw_selector):
    def _el():
        wait = WebDriverWait(get_appium_driver(), 10)
        selector = locator_for_platform(raw_selector)
        return wait.until(EC.presence_of_all_elements_located(selector))

    return _el


def element(raw_selector: dict):
    def _element():
        driver = get_appium_driver()
        return driver.find_element(*locator_for_platform(raw_selector))

    return _element


def locator_for_platform(selectors: dict):
    return selectors.get(configs.PLATFORM)
