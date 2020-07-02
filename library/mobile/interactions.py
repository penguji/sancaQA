from time import sleep

from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from library.mobile import configs, ui
from library.mobile.drivers import get_driver


def action_on_element(element, action, *args):
    getattr(element, action)(args)


def as_element(something=None, at: tuple = None, raise_error=True):
    if something is None and at is not None:
        return driver().find_element(*at)
    if isinstance(something, tuple):
        return driver().find_element(*something)
    if isinstance(something, str):
        return find_text(something, at, raise_error)
    if is_element(something):
        return something


def click(text=None, at: tuple = None):
    as_element(text, at).click()
    sleep(1)  # wait animation done


def driver():
    return get_driver()


def find_text(something: str, inside_selector: tuple = None, raise_error=True):
    # when something is a text
    selector = {
        "android": f"//*[@text='{something}']",
        "ios": f"//*[@label='{something}' and @visible='true']",
    }.get(configs.PLATFORM)
    context = (
        driver() if not inside_selector else driver().find_element(inside_selector)
    )
    elements = context.find_elements(by=By.XPATH, value=selector)
    if len(elements) > 0:
        return elements[0]
    else:
        if raise_error:
            raise NoSuchElementException(f'Element by text "{something}" is not found')
        else:
            return False


def go_back():
    driver().back()


def grab_orientation():
    pass


def grab_text(at):
    el = as_element(at)
    return el.text


def hide_keyboard():
    sleep(1)
    # 'pressKey', 'Done'
    # driver().hide_keyboard(strategy='tapOutside')


def is_element(element_or_elements):
    if isinstance(element_or_elements, ui.Element):
        return True
    elif isinstance(element_or_elements, ui.Elements):
        return True
    else:
        return False


def open_notification():
    pass


def perform_swipe(x, y):
    pass


def set_network(mode: int):
    """
    0 // airplane mode off, wifi off, data off
    1 // airplane mode on, wifi off, data off
    2 // airplane mode off, wifi on, data off
    4 // airplane mode off, wifi off, data on
    6 // airplane mode off, wifi on, data on
    """
    pass


def set_orientation(orientation: str):
    # orientation ("LANDSCAPE" | "PORTRAIT")
    pass


def shake_device():
    pass


def start_activity(name: str):
    pass


def swipe(direction: str):
    # direction (DOWN | UP | LEFT | RIGHT)
    pass


def swipe_to(at):
    pass


def verify_current_activity(name: str):
    pass


def verify_not_see(something, at: tuple = None):
    is_found = as_element(something, at, False)
    assert not is_found, f"Element '{something}' should not visible"


def verify_see(something, at: tuple = None):
    is_found = as_element(something, at, False)
    if is_found:
        assert is_found.is_displayed()
        return True
    else:
        raise WebDriverException(f"Element {something} should visible")


def wait_for_element(at, until: int = 3):
    selector = at if not is_element(at) else at.selector
    assert isinstance(selector, tuple)
    waiter = WebDriverWait(driver(), until)
    return waiter.until(EC.presence_of_element_located(selector))


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


tap = click  # Alias
