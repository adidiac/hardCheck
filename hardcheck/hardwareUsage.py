import shutil
import psutil
import os.path
from os import path
def cpuOverUsage():
    """Check if is more than 50% usage of cpu in interval of 2 seconds and returns a tuple with False and a message if less than 50%\n
    True and a message otherwise\n
    more on https://psutil.readthedocs.io/en/latest/"""
    cpuPercent=psutil.cpu_percent(2)
    if cpuPercent<50:
        isOverUsage=False
        message="It's using less than 50%"
        return (isOverUsage,message)
    else:
        isOverUsage=True
        message="It's using more than 50%"
        return (isOverUsage,message)


def diskOverUsage(partition):
    """Check if is more than 50% usage of disk on certain partition and returns a tuple with False and a message if less than 50%\n
        True and a message otherwise\n
        If partition doesn't exist raise a ValueError\n
        more on https://docs.python.org/3/library/shutil.html"""
    if path.exists(partition):
        memory=shutil.disk_usage(partition)
        diskPercent=(memory.used/memory.total)*100
        if diskPercent<50:
            isOverUsage=False
            message="It's using less than 50%"
            return (isOverUsage,message)
        else:
            isOverUsage=True
            message="It's using more than 50%"
            return (isOverUsage,message)
    else:
        raise ValueError("The path doesn't exists")
        