from time import sleep

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from library.mobile import configs, ui
from library.mobile.drivers import get_driver
from library.mobile.ui import MobileElementPatch


def driver():
    return get_driver()


def go_back():
    driver().back()


def is_element(element_or_elements):
    if isinstance(element_or_elements, ui.Element):
        return True
    elif isinstance(element_or_elements, ui.Elements):
        return True
    else:
        return False


def find_text(something: str, inside_selector: tuple = None, raise_error=True):
    # when something is a text
    selector = {
        "android": f"//*[@text='{something}']",
        "ios": f"//*[@label='{something}' and @visible='true']"
    }.get(configs.PLATFORM)
    context = driver() if not inside_selector else driver().find_element(inside_selector)
    elements = context.find_elements(by=By.XPATH, value=selector)
    if len(elements) > 0:
        return elements[0]
    else:
        if raise_error:
            raise NoSuchElementException(f'Element by text "{something}" is not found')
        else:
            return False


def as_element(something=None, at: tuple = None, raise_error=True):
    if something is None and isinstance(at, tuple):
        return driver().find_element(*at)

    if isinstance(something, str):
        return find_text(something, at, raise_error)
    if is_element(something):
        return something


def action_on_element(element, action, *args):
    getattr(element, action)(args)


def click(text=None, at: tuple = None):
    as_element(text, at).click()
    sleep(1)  # wait animation done


tap = click  # Alias


def verify_see(something, at: tuple = None):
    is_found = as_element(something, at, False)
    if is_found:
        assert is_found.is_displayed()
        return True
    else:
        raise WebDriverException(f"Element {something} should visible")


def verify_not_see(something, at: tuple = None):
    is_found = as_element(something, at, False)
    assert not is_found,  f"Element '{something}' should not visible"


def write(text, at=None, enter=False):
    if not at:
        raise Exception("Need given element/selector 'at'")

    element = None
    if is_element(at):
        element = at
    if isinstance(at, tuple):
        # when context is locator
        element = driver().find_element(*at)
    element.send_keys(text)
    if enter:
        element.send_keys(Keys.ENTER)
    else:
        hide_keyboard()


def hide_keyboard():
    sleep(1)
    # driver().hide_keyboard(strategy='tapOutside')