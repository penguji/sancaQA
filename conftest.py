import pytest
import os
from appium import webdriver
from app import devices

PATH = lambda p: os.path.abspath(
	os.path.join(os.path.dirname(__file__), p)
)

@pytest.fixture()
def driver_setup(request):
	_capabilities = {
		'ANDROID': {
			'platformName': 'Android',
			'platformVersion': devices.ANDROID_VERSION,
			'deviceName': devices.ANDROID_DEVICE_NAME,
			'noReset': True,
			'newCommandTimeout': devices.APPIUM_TIMEOUT,
			'automationName': 'UiAutomator2',
			'appPackage': devices.ANDROID_APP_PACKAGE,
			'appActivity': devices.ANDROID_APP_ACTIVITY,
			'browserName': ''
		},
		'IOS': {
			'version': '',
			'platformName': '',
			'platformVersion': '',
			'deviceName': '',
			'app': '',
			'noReset': '',
			'fullReset': '',
			'newCommandTimeout': ''
		}
	}.get(devices.PLATFORM)

	print('_capabilities sekarang:',_capabilities)

	request.instance.driver = webdriver.Remote(
		command_executor=devices.APPIUM_SERVER,
		desired_capabilities=_capabilities
	)

	yield

	print('proses teardown')
	request.instance.driver.quit()
