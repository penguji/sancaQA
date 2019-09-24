import pytest

from screens.login import Login


@pytest.mark.usefixtures('driver_setup')
class TestAuthentication:
	def test_invalid_login(self):
		print("ini adalah test  pertamax gan")
		login_screen = Login(self.driver)
		login_screen.submit('0899', 'katasandi')
		breakpoint()

	def test_empty_data(self):
		print("fill with blank data")
