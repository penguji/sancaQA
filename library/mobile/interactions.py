from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from library.mobile import configs, ui
from library.mobile.configs import LOGGER
from library.mobile.drivers import get_driver
from library.mobile.ui import Element, Elements


def _selector_by_text(text: str, case_sensitive=True):
    selector_strict = {
        "android": f"//*[@text='{text}']",
        "ios": f"//*[@label='{text}' and @visible='true']",
    }.get(configs.PLATFORM)
    selector_case_insensitive = {
        "android": f"//*[lower-case(@text)='{text.lower()}']",
        "ios": f"//*[@label='{text.lower()}' and @visible='true']",
    }.get(configs.PLATFORM)

    return selector_strict if case_sensitive else selector_case_insensitive


def _transform_element(
    candidate=None,
    at: tuple = None,
    wait: int = 1,
    return_array: bool = False,
    case_sensitive=True,
):
    """Transforms a text or tuple into Element/s
    sample usage:
        _transform_element("Save")
        _transform_element(('xpath', '//locator'))
        _transform_element(home.SEARCH_INPUT)
    """

    if is_element(candidate):
        if wait > candidate.wait_time:
            # when new wait is bigger than default
            LOGGER.warning(f"=====> Updating wait time {candidate.wait_time} => {wait}")
            candidate.wait_time = wait
        LOGGER.info(f'    by selector: "{candidate.selector}"')
        return candidate

    selector = None
    if at and candidate is None:
        selector = at
    if isinstance(candidate, tuple):
        selector = candidate
    if isinstance(candidate, str):
        selector = (
            "xpath",
            _selector_by_text(candidate, case_sensitive=case_sensitive),
        )

    LOGGER.info(f'    by Selector: "{selector}"')
    if return_array:
        return Elements(android_by=selector, ios_by=selector, wait_time=wait)
    else:
        return Element(android_by=selector, ios_by=selector, wait_time=wait)


def click(text=None, at: tuple = None):
    LOGGER.info(f"==> Clicking {text}")
    _transform_element(text, at).click()
    sleep(1)  # wait animation done


def find_text(text: str, inside_selector: tuple = None, raise_error=True):
    # when something is a text
    LOGGER.info(f'==> Finding text: "{text}"')
    selector = {
        "android": f"//*[@text='{text}']",
        "ios": f"//*[@label='{text}' and @visible='true']",
    }.get(configs.PLATFORM)
    context = (
        get_driver()
        if not inside_selector
        else get_driver().find_element(inside_selector)
    )
    elements = context.find_elements(by=By.XPATH, value=selector)
    if len(elements) > 0:
        return elements[0]
    else:
        if raise_error:
            raise NoSuchElementException(f'Element by text "{text}" is not found')
        else:
            return False


def go_back():
    LOGGER.info("==> Going back")
    get_driver().back()


def grab_orientation():
    pass


def grab_text(at):
    LOGGER.info(f"==> Grabing text {at}")
    el = _transform_element(at)
    return el.text


def hide_keyboard():
    LOGGER.info("==> Hiding keyboard")
    sleep(1)
    # 'pressKey', 'Done'
    # get_driver().hide_keyboard(strategy='tapOutside')


def is_element(element_or_elements):
    if isinstance(element_or_elements, ui.Element):
        return True
    elif isinstance(element_or_elements, ui.Elements):
        return True
    else:
        return False


def open_notification():
    """ Open Android notifications (Emulator only)"""
    LOGGER.info("==> Opening Notification")
    if configs.IS_ANDROID:
        get_driver().open_notifications()


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
    LOGGER.info(f"==> Set network mode: {mode}")
    get_driver().set_network_connection(mode)


def set_orientation(orientation: str):
    # orientation ("LANDSCAPE" | "PORTRAIT")
    assert orientation in ["LANDSCAPE", "PORTRAIT"]
    get_driver().orientation = orientation


def shake_device():
    """Perform a shake action on the device"""
    LOGGER.info("==> Shake device")
    get_driver().shake()


def start_activity(app_package: str, app_activity: str):
    """Start an Android activity by providing package name and activity name"""
    LOGGER.info(f"==> Start activity {app_package}-{app_activity}")
    get_driver().start_activity(app_package, app_activity)


def swipe(direction: str, speed: str = "FAST"):
    # Perform scrolling screen, using 80:20 of the screen size
    # direction (DOWN | UP | LEFT | RIGHT)
    # start from Opposite Direction, e.g swipe UP = start from down screen to up screen
    LOGGER.info(f"==> Swiping {direction} {speed}LY")
    assert direction in ["DOWN", "UP", "LEFT", "RIGHT"]
    assert speed in ["FAST", "MEDIUM", "SLOW"]
    duration = {"FAST": 500, "MEDIUM": 1000, "SLOW": 2000}.get(speed)
    screen_size = get_driver().get_window_size()
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

    # get_driver().swipe(from_x, from_y, to_x, to_y, duration)
    swipe_coordinate(from_x, from_y, to_x, to_y, duration)


def swipe_coordinate(from_x: int, from_y: int, to_x: int, to_y: int, speed: int = 500):
    LOGGER.debug(f"==> Swipe coordiates {from_x, from_y, to_x, to_y, speed}")
    get_driver().swipe(from_x, from_y, to_x, to_y, speed)
    # from selenium.webdriver import TouchActions
    # action = TouchActions(get_driver())
    # action.tap_and_hold(from_x, from_y)
    # action.move(to_x, to_y)
    # action.release(to_x, to_y)
    # action.perform()


def swipe_to(at):
    pass


def verify_current_activity(name: str):
    pass


def verify_not_see(text_or_elements, at: tuple = None, case_sensitive=True):
    LOGGER.info("==> Should NOT see")
    sleep(2)  # wait animation
    elements = _transform_element(
        text_or_elements, at, return_array=True, case_sensitive=case_sensitive
    )
    assert not elements.found, f"Element '{text_or_elements}' should NOT BE visible"


def verify_see(text_or_elements, at: tuple = None, case_sensitive=True):
    LOGGER.info("==> Should see")
    sleep(2)  # wait animation
    el = _transform_element(
        text_or_elements, at, return_array=True, case_sensitive=case_sensitive
    )
    assert el.found > 0, f"Element {el.selector} is NOT visible"


def wait_for_element(at, until: int = 3):
    LOGGER.info(f"==> Wait for element for {until}s")
    el = _transform_element(at, wait=until)
    el.is_displayed()


def write(text, at=None, enter=False):
    LOGGER.info(f"==> Writing {text} at {at}")
    if not at:
        raise Exception("Need given element/selector 'at'")

    element = _transform_element(at)
    element.send_keys(text)
    if enter:
        element.send_keys(Keys.ENTER)
    else:
        hide_keyboard()


tap = click  # Alias
