from appium import webdriver

from library import configs, parallel
from library.configs import APPIUM_SERVER
from library.devices import get_device_id


class SingletonFactory(object):
    """
    A factory of the same instances of injected classes.
    """

    # a mapping between the name of a class and the instance.
    mappings = {}

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
        if str(device_id) in SingletonFactory.mappings:
            instance_ = SingletonFactory.mappings[str(device_id)]
        # else create the instance and map it to the class name.
        else:
            instance_ = webdriver.Remote(**constructor_args)
            SingletonFactory.mappings[str(device_id)] = instance_

        return instance_


def get_appium_server():
    ports = [4723, 4724, 4725]
    return APPIUM_SERVER.format(parallel.device_index(ports))


def get_appium_driver() -> webdriver.Remote:
    """
    Return the same instance to the Appium driver.
    """
    return SingletonFactory.build(
        get_device_id(),
        command_executor=get_appium_server(),
        desired_capabilities=configs.CAPABILITIES,
    )


def close_appium_driver():
    """
    Close Mobile app and delete reference at singleton, so device_id can re-initiate
    """
    driver = get_appium_driver()
    driver.quit()
    SingletonFactory.mappings.pop(get_device_id())
