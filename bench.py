#!/usr/bin/env python
import os, sys
script_path = os.path.realpath(__file__)
bb_path = os.path.dirname(script_path)
sys.path.append(os.path.join(bb_path, 'src'))
import beaglebench as bb

class Commands:
    __doc__ =  """
        Commands are implemented as methods in this object

        Some commands may take arguments.
        E.g. If you know your SD card is on /dev/sdb you could go
            ./bb sd /dev/sdb
        and /dev/sdb will be passed in as the device_node

        Any communication with the BeagleBone is via SSH by means of the USB network

        Add more functionality by editing %s
        """ % script_path

    def sd(self, device_node=None):
        '''Interactively prepare an SD card'''
        bb.make_sd(device_node)

    def setup(self):
        '''Transfer and run all setup scripts on the BeagleBone'''
        bb.remotely_run_scripts_in('setup')

    def test(self):
        '''Transfer and run all test scripts on the BeagleBone'''
        bb.remotely_run_scripts_in('test')

    def reboot(self):
        '''Reboot the BeagleBone'''
        bb.reboot_beaglebone()

    def ssh(self):
        '''SSH into the BeagleBone'''
        bb.ssh()

def cli(klass, n=0):
    __name__ = "BeagleBench CLI"
    action = None
    try: action = getattr(klass(), sys.argv[1+n])
    except IndexError: help(klass)
    except AttributeError: help(klass)
    if (action):
        try: return action(*sys.argv[2+n:len(sys.argv)])
        except KeyboardInterrupt: sys.exit(1)

if __name__ == "__main__": cli(Commands)
