#!/usr/bin/env python
import os, sys, subprocess

bb_path = os.path.join(os.environ['HOME'], 'beaglebench')

try:
    import beaglebench
except ImportError:
    print "Beaglebench is not installed. Installing it into %s/.beaglebench" % bb_path
    subprocess.call(['git', 'clone', 'https://github.com/fatehitech/beaglebench', '.beaglebench'])

class Bench:
    def sd(self):
        subprocess.call(["bash", ".beaglebench/Image/make-sd.sh"])


if __name__ == "__main__":
    try:
        bench = Bench()
        cmd = sys.argv[1]
        getattr(bench, cmd)()
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
