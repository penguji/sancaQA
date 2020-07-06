import os
import logging

from dotenv import load_dotenv

from library.mobile.devices import android_udid

load_dotenv()
LOGGER = logging.getLogger()

APPIUM_TIMEOUT = 300
APPIUM_SERVER = os.getenv("APPIUM_SERVER")
PLATFORM = os.getenv("TEST_PLATFORM", "android").lower()
APP_CAPS = os.getenv("TEST_CAPS")
IS_ANDROID = PLATFORM.upper() == "ANDROID"
IS_IOS = PLATFORM.upper() == "IOS"
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_TIMEOUT", "3"))
IS_RUN_REMOTE = os.getenv("TEST_REMOTE", "false").lower() == "true"
PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
)


def load_caps(platform: str, app_caps: str = None):
    import json

    # Load default capabilities per platform
    caps_path = os.path.join(PROJECT_PATH, "configs", "capabilities.json")
    with open(caps_path) as caps_file:
        default_caps = json.load(caps_file).get(platform)

    if app_caps:
        # Load and update additional caps for given apps name (file)
        app_caps_path = os.path.join(PROJECT_PATH, "configs", app_caps)
        with open(app_caps_path) as caps_file:
            app_caps = json.load(caps_file).get(platform)
            default_caps.update(app_caps)

        if IS_IOS:
            pass
        else:
            default_caps["udid"] = android_udid()

    return default_caps


CAPABILITIES = load_caps(PLATFORM, APP_CAPS)
