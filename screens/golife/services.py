from screens.golife import errors


def verify_service_not_available():
    assert (
        str(errors.ERROR_TITLE.text).strip() == "Layanan ini sementara tidak tersedia"
    )
    assert (
        str(errors.ERROR_DESCRIPTION.text).strip()
        == "Sebagai antisipasi penyebaran COVID-19, kami menghentikan layanan GoMassage untuk sementara di semua wilayah. Keamanan & keselamatan semua pihak merupakan prioritas utama kami."  # noqa
    )
