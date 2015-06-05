import os, stat
import platform_specific as helpers
from sys import platform as _platform

def select(device_node, node=""):
    if _platform == 'darwin':
        print "Kernel installation is untested on Mac. Use a linux machine or, if you're a developer, add Mac support by reading the code as it will be executed from this point on and replace any non-Mac commands with their Mac equivalents."
    else:
        helpers.listBlockDevices()
        prompt = "Enter the top-level device path of SD card (e.g. /dev/sdb): "
        while not is_block_device(node): node = raw_input(prompt).strip()
        return node

def is_block_device(filename):
    if not filename: return False
    try:
        mode = os.lstat(filename).st_mode
    except OSError:
        return False
    else:
        return stat.S_ISBLK(mode)
