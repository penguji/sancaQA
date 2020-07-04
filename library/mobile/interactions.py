from time import sleep

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from library.mobile import configs, ui
from library.mobile.configs import LOGGER
from library.mobile.drivers import get_driver


def action_on_element(element, action, *args):
    getattr(element, action)(args)


def _transform_element(something=None, at: tuple = None, raise_error=True):
    if something is None and at is not None:
        return driver().find_element(*at)
    if isinstance(something, tuple):
        return driver().find_element(*something)
    if isinstance(something, str):
        return find_text(something, at, raise_error)
    if is_element(something):
        return something


def click(text=None, at: tuple = None):
    LOGGER.info(f'==> Clicking {text}')
    _transform_element(text, at).click()
    sleep(1)  # wait animation done


def driver():
    return get_driver()


def find_text(something: str, inside_selector: tuple = None, raise_error=True):
    # when something is a text
    LOGGER.info(f'==> Finding text: "{something}"')
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
    LOGGER.info('==> Going back')
    driver().back()


def grab_orientation():
    pass


def grab_text(at):
    LOGGER.info(f'==> Grabing text')
    el = _transform_element(at)
    return el.text


def hide_keyboard():
    LOGGER.info(f'==> Hiding keyboard')
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
    # Open Android notifications (Emulator only)
    LOGGER.info('==> Opening Notification')
    if configs.IS_ANDROID:
        driver().open_notifications()


def perform_swipe(x, y):
    pass


def set_network(mode: int):
    """Sets the network connection type. Android only.
    0 // airplane mode off, wifi off, data off
    1 // airplane mode on, wifi off, data off
    2 // airplane mode off, wifi on, data off
    4 // airplane mode off, wifi off, data on
    6 // airplane mode off, wifi on, data on
    """
    LOGGER.info(f'==> Set network mode: {mode}')
    driver().set_network_connection(mode)


def set_orientation(orientation: str):
    # orientation ("LANDSCAPE" | "PORTRAIT")
    assert orientation in ["LANDSCAPE", "PORTRAIT"]
    driver().orientation = orientation


def shake_device():
    """Perform a shake action on the device"""
    LOGGER.info('==> Shake device')
    driver().shake()


def start_activity(app_package: str, app_activity: str):
    """Start an Android activity by providing package name and activity name"""
    LOGGER.info(f'==> Start activity {app_package}-{app_activity}')
    driver().start_activity(app_package, app_activity)


def swipe(direction: str, speed: str = "FAST"):
    # Perform scrolling screen, using 80:20 of the screen size
    # direction (DOWN | UP | LEFT | RIGHT)
    # start from Opposite Direction, e.g swipe UP = start from down screen to up screen
    LOGGER.info(f'==> Swiping {direction} {speed}LY')
    assert direction in ["DOWN", "UP", "LEFT", "RIGHT"]
    assert speed in ["FAST", "MEDIUM", "SLOW"]
    duration = {"FAST": 500, "MEDIUM": 1000, "SLOW": 2000}.get(speed)
    screen_size = driver().get_window_size()
    width, height = int(screen_size["width"]), int(screen_size["height"])
    from_x, to_x, from_y, to_y = 0, 0, 0, 0
    if direction == "UP":
        from_x = int(width * 0.5)  # center at screen 50%
        to_x = from_x
        from_y = int(height * 0.8)  # start 80% screen
        to_y = int(height * 0.2)  # end 20% screen
    elif direction == "DOWN":
        from_x = int(width * 0.5)  # center at screen 50%
        to_x = from_x
        from_y = int(height * 0.2)  # start 20% screen
        to_y = int(height * 0.8)  # end 80% screen

    # driver().swipe(from_x, from_y, to_x, to_y, duration)
    swipe_coordinate(from_x, from_y, to_x, to_y, duration)


def swipe_coordinate(from_x: int, from_y: int, to_x: int, to_y: int, speed: int = 500):
    LOGGER.debug(f'==> Swipe coordiates {from_x, from_y, to_x, to_y, speed}')
    driver().swipe(from_x, from_y, to_x, to_y, speed)
    # from selenium.webdriver import TouchActions
    # action = TouchActions(driver())
    # action.tap_and_hold(from_x, from_y)
    # action.move(to_x, to_y)
    # action.release(to_x, to_y)
    # action.perform()


def swipe_to(at):
    pass


def verify_current_activity(name: str):
    pass


def verify_not_see(something, at: tuple = None):
    LOGGER.info(f'==> Should NOT see {something}')

    is_found = _transform_element(something, at, False)
    assert not is_found, f"Element '{something}' should not visible"


def verify_see(something, at: tuple = None):
    LOGGER.info(f'==> Should see {something}')
    is_found = _transform_element(something, at, False)
    if is_found:
        assert is_found.is_displayed()
        return True
    else:
        raise WebDriverException(f"Element {something} should visible")


def wait_for_element(at, until: int = 3):
    LOGGER.info(f'==> Wait for element {at} for {until}s')
    selector = at if not is_element(at) else at.selector
    assert isinstance(selector, tuple)
    waiter = WebDriverWait(driver(), until)
    return waiter.until(EC.presence_of_element_located(selector))


def write(text, at=None, enter=False):
    LOGGER.info(f'==> Writing {text} at {at}')
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
