"""
Alternative Page object as in login_screen.py file
"""

from library.mobile.ui import Element, Elements

BTN_LOGIN = Element(android_by=("id", "btn_login"), ios_by=("id", "btn_logs"))
BTN_SIGNUP = Element(android_by=("id", "btn_signup"), wait_time=True)
TXT_ALL = Elements(android_by=("xpath", "//android.widget.TextView"))
