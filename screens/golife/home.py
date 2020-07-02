from library.mobile.ui import Element

SERVICE_GOMASSAGE = Element(android_by=('id', 'viewVertical1'))
SERVICE_GOCLEAN = Element(android_by=('id', 'viewVertical2'))
SERVICE_RIBBON = Element(android_by=('id', 'ribbonBadge'))


def open_service(name: str):
    service_name = {
        'gomassage': SERVICE_GOMASSAGE,
        'goclean': SERVICE_GOCLEAN
    }.get(name.lower())
    service_name.click()