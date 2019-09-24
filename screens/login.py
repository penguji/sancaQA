from screens.base import Screen


class Login(Screen):
	input_login = ('id', 'input_field')
	btn_login = ('id', 'button_signin')

	def submit(self, phone, password):
		self.input_login
		self.click(self.btn_login)
