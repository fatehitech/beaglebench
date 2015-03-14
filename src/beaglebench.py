import os, subprocess, repo, glob
from sd import make as makeSD

os.environ['BEAGLEBONE_USER'] = "root"
os.environ['BEAGLEBONE_HOST'] = "192.168.7.2"

def remotelyRunScriptsIn(dirpath):
    if os.path.isdir(dirpath):
        shellscripts = glob.glob(dirpath+'/*.sh')
        if len(shellscripts) > 0:
            helpers = repo.root+'/support/helpers.sh'
            subprocess.call(['bash', '-c', 'source '+helpers+' && remotely_run_scripts_in '+dirpath])
        else:
            print dirpath+" has no files ending in .sh"
    else:
        print "No such directory: " +dirpath

def rebootBeagleBone():
    subprocess.call(['bash', '-c', "ssh -o ConnectTimeout=1 -o LogLevel=Error $BEAGLEBONE_USER@$BEAGLEBONE_HOST reboot"])
