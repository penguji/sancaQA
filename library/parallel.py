import os
import random

NUMBER: str = os.getenv("PYTEST_XDIST_WORKER", "gw0")
COUNT: str = os.getenv("PYTEST_XDIST_WORKER_COUNT", "0")  # Return 2 if `-n 2` is passed
IS_PARALLEL: bool = COUNT != "0"


def worker_index():
    idx = int(NUMBER[2:])  # will extract number in workername e.g gw3
    if idx > int(COUNT):
        return 0
    return idx


def device_index(list_device: list):
    # prevent index more than available devices
    index = worker_index()
    max_device = len(list_device)
    if index >= max_device:
        shuffle = random.randint(1, max_device)
        index = shuffle - 1  # used for array, reduce 1
    return list_device[index]
