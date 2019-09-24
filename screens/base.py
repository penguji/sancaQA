from appium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Screen:
	def __init__(self, driver: Remote):
		self.driver = driver

	def get_element(self, _locator):
		"return element from locator (in tuple)"

		method = _locator[0]
		locator = _locator[1]

		if type(locator) is str:
			return self.get_element_by_type(method, locator)

	def get_element_by_type(self, method, locator):
		if method == 'accesibility_id':
			return self.driver.find_element_by_accessibility_id(locator)
		elif method == 'android':
			return self.driver.find_element_by_android_uiautomator('new UiSelector().%s' % locator)
		elif method == 'ios':
			return self.driver.find_element_by_ios_uiautomation(locator)
		elif method == 'xpath':
			return self.driver.find_element_by_xpath(locator)
		elif method == 'id':
			print('==> check by ID')
			return self.driver.find_element_by_id(locator)
		elif method == 'class_name':
			return self.driver.find_element_by_class_name(locator)
		elif method == 'name':
			return self.driver.find_element_by_name(locator)
		else:
			raise Exception('Invalid locator type')

	def wait_visible(self, locator, timeout=0):
		i = 0
		while i != timeout:
			try:
				self.is_visible(locator)
				return self.get_element(locator)
			except NoSuchElementException:
				sleep(1)
				i += 1

	def is_visible(self, locator):
		try:
			self.get_element(locator).is_displayed()
			return True
		except NoSuchElementException:
			return False

	def click(self, locator):
		# element = self.wait_visible(locator)
		print("ngeClick")
		sleep(5)
		element = self.get_element(locator)
		element.click()
