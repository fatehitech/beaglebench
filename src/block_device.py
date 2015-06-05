import os, stat
import platform_specific as helpers
from sys import platform as _platform

def select(device_node, node=""):
    while not is_block_device(node):
        helpers.listBlockDevices()
        helpers.print2("Enter the top-level device path of SD card (e.g. /dev/sdb): ")
        node = raw_input().strip()
    return node

def is_block_device(filename):
    if not filename: return False
    try:
        mode = os.lstat(filename).st_mode
    except OSError:
        return False
    else:
        return stat.S_ISBLK(mode)
