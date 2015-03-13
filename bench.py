#!/usr/bin/env python
import os, sys, subprocess

bb_upstream = "https://github.com/fatehitech/beaglebench"
bb_path = os.path.join(os.environ['HOME'], '.beaglebench')
sys.path.append(os.path.join(bb_path, 'src'))

try:
    import beaglebench as bb
except ImportError:
    print "Beaglebench is not installed. Installing it into %s/.beaglebench" % bb_path
    subprocess.call(['git', 'clone', bb_upstream, bb_path])
    import beaglebench as bb

class Commands:
    def sd(self):
        bb.makeSD()

if __name__ == "__main__":
    try:
        getattr(Commands(), sys.argv[1])()
    except IndexError:
        print "No command given"


#	git clone https://github.com/fatehitech/beaglebench .beaglebench
#	bash -c "pushd .beaglebench && git pull origin master && popd"
#
#sd:
#	
#
#setup:
#	bash -c "source Support/helpers.sh; remotely_run_scripts_in SetupScripts"
#
#test:
#	.beaglebench/test
#
#reboot:
#	ssh -o ConnectTimeout=1 -o LogLevel=Error root@192.168.7.2 reboot
#
#halt:
#	ssh -o ConnectTimeout=1 -o LogLevel=Error root@192.168.7.2 halt
