import subprocess

from library import shell
from library.devices import get_device_id
from library.parallel import IS_PARALLEL

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


def get_device_id():
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
