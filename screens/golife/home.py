from library.mobile.ui import Element, Elements

SERVICE_GOMASSAGE = Element(android_by=("id", "viewVertical1"), wait_time=5)
SERVICE_GOCLEAN = Element(android_by=("id", "viewVertical2"), wait_time=5)
SERVICE_RIBBON = Element(android_by=("id", "ribbonBadge"))
GOPAY_BALANCE = Element(android_by=("id", "tvGoPay"))
SEARCH_BAR = Element(android_by=("id", "input"), wait_time=5)
NAVIGATIONS_LABELS = Elements(android_by=('id', 'smallLabel'))


def open_service(name: str):
    service_name = {"gomassage": SERVICE_GOMASSAGE, "goclean": SERVICE_GOCLEAN}.get(
        name.lower()
    )
    service_name.click()
