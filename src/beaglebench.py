import os, glob, helper
from sd import make as make_sd

def remotely_run_scripts_in(dirpath):
    if not os.path.isdir(dirpath): print "No such directory: " +dirpath
    else:
        shellscripts = glob.glob(dirpath+'/*.sh')
        if len(shellscripts) is 0: print dirpath+" has no files ending in .sh"
        else:
            status = helper.call('remotely_run_scripts_in '+dirpath)
            if status is 0: pass
            else: print "ERROR: Remote script exited with non-zero status %d" % status

def reboot_beaglebone():
    helper.call('reboot_beaglebone')

def ssh():
    helper.call('ssh_beaglebone')
