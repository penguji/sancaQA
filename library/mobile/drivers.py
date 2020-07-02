from appium import webdriver

from library.mobile import configs, parallel
from library.mobile.devices import get_device_id


class SingletonFactory(object):
    """
    A factory of the same instances of injected classes.
    """

    # a mapping between the name of a class and the instance.
    mappings = {}

    @staticmethod
    def get_instance(device_id: str):
        if device_id in SingletonFactory.mappings:
            return SingletonFactory.mappings[device_id]
        else:
            return None

    @staticmethod
    def build(device_id, **constructor_args):
        """
        Builds an instance of the given class pointer together with the provided constructor arguments.
        Returns the SAME instance for a given class.

        :param device_id: A pointer to the device driver instance.
        :param constructor_args: The arguments for the class instance.
        :return: An instance of the provided class.
        """

        # if the class instance is mapped, then retrieve it.
        instance_ = SingletonFactory.get_instance(device_id)
        # else create the instance and map it to the class name.
        if not instance_:
            instance_ = webdriver.Remote(**constructor_args)
            SingletonFactory.mappings[str(device_id)] = instance_

        return instance_


def get_appium_server():
    import json
    import os

    # Load default capabilities per platform
    caps_path = os.path.join(configs.PROJECT_PATH, "configs", "capabilities.json")
    with open(caps_path) as caps_file:
        appium_config = json.load(caps_file).get("appium")
    port = parallel.device_index(appium_config["availablePorts"])
    return "http://{0}:{1}/wd/hub".format(appium_config["ip"], port)


def create_appium_session(udid: str, capabilities: dict):
    return SingletonFactory.build(
        udid, command_executor=get_appium_server(), desired_capabilities=capabilities,
    )


def get_driver(udid: str = get_device_id()) -> webdriver.Remote:
    """
    Return the same instance to the Appium driver.
    """
    if udid in SingletonFactory.mappings:
        return SingletonFactory.mappings[udid]
    else:
        return create_appium_session(get_device_id(), configs.CAPABILITIES)


def quit_driver():
    """
    Close Mobile app and delete reference at singleton, so device_id can re-initiate
    """
    udid = get_device_id()
    driver = get_driver(udid)
    driver.quit()
    SingletonFactory.mappings.pop(udid)
