import os


def env_get(key, default=None):
	return os.environ.get(key=key, default=default)


def env_get_bool(key, default=None):
	value = env_get(key, default)
	return f'{value}'.lower() == 'true'


APPIUM_TIMEOUT = env_get('APPIUM_TIMEOUT', 3600)
APPIUM_SERVER = env_get('APPIUM_SERVER', 'http://0.0.0.0:4723/wd/hub')
PLATFORM = env_get('PLATFORM', 'ANDROID')
IS_ANDROID = PLATFORM == 'ANDROID'
IS_IOS = PLATFORM == 'IOS'

ANDROID_APP_PACKAGE = 'com.instagram.android'
ANDROID_APP_ACTIVITY = 'com.instagram.android.activity.MainTabActivity'

ANDROID_VERSION = env_get('ANDROID_VERSION', '9')
ANDROID_DEVICE_NAME = env_get('ANDROID_DEVICE_NAME', 'Pixel_3a_API_28')

IOS_VERSION = ''
IOS_DEVICE_NAME = ''
