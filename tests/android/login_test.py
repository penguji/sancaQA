import pytest


@pytest.mark.usefixtures('driver_setup')
class TestLogin:
	def test_pertamax(self):
		print("ini adalah kerjaan pertamax gan")
