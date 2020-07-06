from time import sleep

from library.mobile import interactions as I
from screens.golife import home, services


def test_gomassage_service_should_be_closed():
    I.wait_for_element(home.SERVICE_GOMASSAGE, until=5)
    home.open_service("GoMassage")
    services.verify_service_not_available()
    I.go_back()
    gopay = I.grab_text(at=("id", "tvGoPay"))
    assert gopay
    assert home.SERVICE_RIBBON.has_text("Disinfektan")
    assert not home.SERVICE_RIBBON.has_no_text("Disinfektan")


def test_navigation_menu():
    I.wait_for_element(home.SERVICE_GOMASSAGE, until=5)
    I.verify_see("Disinfektan")
    I.tap("Pesanan")
    I.tap("Beranda")
    I.click(home.SEARCH_BAR)
    I.write("motor", at=home.SEARCH_BAR)
    I.go_back()
    gopay2 = I.grab_text(home.GOPAY_BALANCE)
    print(gopay2)
    I.click(at=("id", "input"))
    I.write("mobil", at=("id", "input"))
    I.go_back()


def test_swiping():
    I.wait_for_element(home.SEARCH_BAR, until=5)
    I.tap("Pesanan")
    I.tap("Beranda")
    I.wait_for_element(home.SEARCH_BAR, until=5)
    I.verify_see("Disinfektan")
    I.verify_not_see("Disinfektannnn")
    for nav in home.NAVIGATIONS_LABELS:
        nav.click()
    I.tap("Beranda")
    I.swipe("UP", "SLOW")
    sleep(3)
    I.swipe("DOWN")
    sleep(2)
