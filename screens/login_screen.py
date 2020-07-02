"""
Classical "Page object model" approach
Alternative "Direct module usage" Style as in login.py file
"""

from library.ui import Element, Elements
from screens.BaseScreens import Screens


class Login(Screens):
    btn_login = Element(android_by=('id', 'btn_login'), ios_by=('id', 'btn_logs'))
    btn_signup = Element(android_by=('id', 'btn_signup'), wait_time=True)
    txt_all = Elements(android_by=('xpath', '//android.widget.TextView'))

    def __init__(self):
        super().__init__()

    def go_back(self):
        self.driver.back()

    def ambil_text(self):
        print('Ambil text')
        for txt in self.txt_all:
            print(txt.text)