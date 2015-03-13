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
    Communication with the BeagleBone is conducted via SSH over the USB network
    """

    def sd(self, device_node=None):
        '''Interactively prepare an SD card'''
        bb.makeSD(device_node)

    def setup(self):
        '''Transfer and run all setup scripts on the BeagleBone'''
#	bash -c "source Support/helpers.sh; remotely_run_scripts_in SetupScripts"

    def test(self):
        '''Transfer and run all test scripts on the BeagleBone'''

    def reboot(self):
        '''Reboot the BeagleBone'''
#	ssh -o ConnectTimeout=1 -o LogLevel=Error root@192.168.7.2 reboot


if __name__ == "__main__":
    __name__ = "BeagleBench"
    action = None
    try: action = getattr(Commands(), sys.argv[1])
    except IndexError: help(Commands)
    except AttributeError: help(Commands)
    if (action):
        try: action(*sys.argv[2:len(sys.argv)])
        except KeyboardInterrupt: sys.exit(1)
