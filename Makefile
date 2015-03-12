sd:
	bash Image/make-sd.sh

setup:
	bash -c "source Support/script-runner.sh; run_scripts_in SetupScripts"

test:
	bash -c "source Support/script-runner.sh; run_scripts_in TestScripts"

reboot:
	ssh -o LogLevel=Error root@192.168.7.2 reboot

halt:
	ssh -o LogLevel=Error root@192.168.7.2 halt
