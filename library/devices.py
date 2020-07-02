from library import parallel, configs, shell


def get_adb_devices():
    android_devices_list = []
    for device in shell.invoke("adb devices").splitlines():
        if "device" in device and "devices" not in device:
            device = device.split("\t")[0]
            android_devices_list.append(device)
    return android_devices_list


def android_udid():
    # support 2 device parallel for now
    if configs.IS_RUN_REMOTE:
        devices = udid_from_configs(configs.PLATFORM)
    else:
        devices = get_adb_devices()
    return parallel.device_index(devices)


def iphone_udid() -> str:
    list_simulator = udid_from_configs('ios')
    return parallel.device_index(list_simulator)


def get_device_id() -> str:
    if configs.IS_IOS:
        return iphone_udid()
    else:
        return android_udid()


def wda_port() -> int:
    available_ports = [8100, 8101]
    return parallel.device_index(available_ports)


def udid_from_configs(platform: str):
    import json
    import os
    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # Load default capabilities per platform
    caps_path = os.path.join(project_path, "configs", "devices.json")
    with open(caps_path) as caps_file:
        device_list = json.load(caps_file).get(platform)

    return [dev['udid'] for dev in device_list]
