from time import sleep
from library.mobile import interactions as I
from screens.golife import home, services


def test_gomassage_service_should_be_closed():
    print('Test GoMassage')
    home.open_service('GoMassage')
    services.verify_service_not_available()
    I.go_back()
    I.verify_see('Disinfektan')
    I.click(at=('id', 'input'))
    I.write('mobil', at=('id', 'input'))
    I.go_back()
    I.verify_not_see('Disinfektannnn')
    I.tap('Pesanan')
    I.tap('Beranda')
    home.SERVICE_RIBBON.has_text('Disinfektan')
    home.SERVICE_RIBBON.has_no_text('Disinfektan')
    I.tap(home.SERVICE_GOCLEAN)
    I.go_back()

    # home.SERVICE_GOMASSAGE


def test_open_goclean_service():
    sleep(5)
    print('Test GoClean')
    pass
