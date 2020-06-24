from library import parallel, configs, shell


def get_android_devices():
    android_devices_list = []
    for device in shell.invoke("adb devices").splitlines():
        if "device" in device and "devices" not in device:
            device = device.split("\t")[0]
            android_devices_list.append(device)
    return android_devices_list


def android_udid():
    # support 2 device parallel for now
    return parallel.device_index(get_android_devices())


def iphone_device_name() -> str:
    list_simulator = ["iPhone 8", "iPhone 8 - 8100", "iPhone 8 - 8101"]
    return parallel.device_index(list_simulator)


def get_device_id() -> str:
    if configs.IS_IOS:
        return iphone_device_name()
    else:
        return android_udid()


def wda_port() -> int:
    available_ports = [8100, 8101]
    return parallel.device_index(available_ports)
