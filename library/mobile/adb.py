from library.mobile import configs, shell
from library.mobile.devices import get_device_id
from library.mobile.parallel import IS_PARALLEL

ADB = "adb {}"
if IS_PARALLEL:
    ADB = f"adb -s {get_device_id()} " + "{}"


def adb(args: str):
    return shell.invoke(ADB.format(args.strip()))


def adb_shell(args: str):
    adb_command = f" shell {args}"
    return adb(adb_command)


def get_device_state():
    """
    Get device status： offline | bootloader | device
    """
    return adb("get-state")


def connect_android_tcp(ip):
    """
    Bind device information for wireless testing
    """
    adb("tcpip 5555")
    return adb("connect {0}:5555".format(ip))


def disconnect_android_tcp(self, ip):
    """
    Release device information for wireless test
    """
    adb("tcpip 5555")
    return adb("disconnect {0}:5555".format(ip))


def get_serial_no():
    """
    Get device id，return serialNo
    """
    return adb("get-serialno")


def get_android_version():
    """
    Get the Android version number on the device, such as 4.2.2
    """
    return adb_shell("getprop ro.build.version.release")


def get_sdk_version():
    """
    Get device SDK version number
    """
    return adb_shell("getprop ro.build.version.sdk")


def get_android_model():
    """
    Get device model
    """

    return adb_shell("getprop ro.product.model")


def get_android_ip():
    """
    Get device IP
    """
    # return adb_shell('netcfg | find "wlan0"').strip().split()[2].split('/')[0]
    return adb_shell('netcfg | find "wlan0"')


def get_rcepageage_version():
    """
    :return: (Version date)
    """
    return adb_shell("dumpsys package cn.rongcloud.rce | findstr version").split()


def app_to_background():
    adb_shell("input keyevent 3")


def app_to_foreground():
    adb_shell(f"monkey -p {configs.APP_NAME} -c android.intent.category.LAUNCHER 1")


def clear_app_data():
    adb_shell(f"pm clear {configs.APP_NAME}")


def close_app():
    adb_shell(f"am force-stop {configs.APP_NAME}")


def grant_revoke_permission(permission_type: str, permission_name: str):
    adb_shell(f"pm {permission_type} {configs.APP_NAME} {permission_name} ")
    pass


def heads_up_notification(enabled=True):
    cmd = "settings put global heads_up_notifications_enabled {}"
    status = "1" if enabled else "0"
    adb_shell(cmd.format(status))


def open_deeplink(url: str):
    adb_shell(f"am start -a android.intent.action.VIEW -d {url}")


def relaunch_app():
    adb_shell(f"am start {configs.APP_NAME}/{configs.APP_ANDROID_ACTIVITY}")


def set_gps(enabled=True):
    cmd = "settings put secure location_providers_allowed {}"
    status = "+gps" if enabled else "-gps"
    adb_shell(cmd.format(status))


def tap_back():
    adb_shell("input keyevent 4")


def tap_at_coordinates(x: int, y: int):
    adb_shell(f"input tap {x} {y}")


def typing(text: str):
    adb_shell(f"input text {text}")


def uninstall_app():
    adb(f"uninstall {configs.APP_NAME}")
