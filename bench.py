#!/usr/bin/env python
import os, sys, subprocess

bb_upstream = "https://github.com/fatehitech/beaglebench"
bb_path = os.path.join(os.environ['HOME'], '.beaglebench')
sys.path.append(os.path.join(bb_path, 'src'))

try:
    import beaglebench as bb
except ImportError:
    subprocess.call(['git', 'clone', bb_upstream, bb_path])
    import beaglebench as bb

class Commands:
    """
    These are all the commands avaiable to you.

    Some commands can take optional arguments.
    E.g. If you know your SD card is on /dev/sdb you could go
        ./bb sd /dev/sdb
    and /dev/sdb will be passed in as the device_node

    Any communication with the BeagleBone is via SSH by means of the USB network
    """

    def sd(self, device_node=None):
        '''Interactively prepare an SD card'''
        bb.makeSD(device_node)

    def setup(self):
        '''Transfer and run all setup scripts on the BeagleBone'''
        bb.remotelyRunScriptsIn('setup')

    def test(self):
        '''Transfer and run all test scripts on the BeagleBone'''
        bb.remotelyRunScriptsIn('test')

    def reboot(self):
        '''Reboot the BeagleBone'''
        bb.rebootBeagleBone()

if __name__ == "__main__":
    __name__ = "BeagleBench CLI"
    action = None
    try: action = getattr(Commands(), sys.argv[1])
    except IndexError: help(Commands)
    except AttributeError: help(Commands)
    if (action):
        try: action(*sys.argv[2:len(sys.argv)])
        except KeyboardInterrupt: sys.exit(1)
