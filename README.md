# beaglebench

This project aims to provide a "workbench-like" experience for people who work with the BeagleBone

The main tool is a python-based task runner (bench.py) that you symlink into your project. It has commands that automate creation of SD cards and run remote scripts like a continuous integration service would (by this I mean that no command in the script fail without your knowledge, and these failures stop the job immediately so you can work fast).

I have found that by using this method of running remote scripts from a pristine, official image, on a real beaglebone, I can achieve more accurate feedback faster than I could get while walking the route in which one builds a custom image at the SD card preparation phase.

If you try this workflow, I recommend that you write your scripts in an idempotent way (same script can be run over and over, on the same machine, without consequence). This way you can have a very tight feedback loop. To learn more about this, check out tools like Ansible and Chef as they are the prime inspiration for beaglebench.

Works in Linux and Mac. You can probably get Windows to work fairly easily if you want. The things that will fail in windows are:

* downloading images (happens during `./bb sd` using `curl`)
* extracting images (happens during `./bb sd` using `unxz`)
* listing block devices (happens during `./bb sd` using `lsblk` or `diskutil list`)
* writing image to block device (happens during `./bb sd` using `dd` with `sudo`)
* running remote scripts (happens during `./bb setup` and `./bb test` using local `bash` to run functions that use `ssh`)

# Requirements

* `python`
* `unxz`
* `curl`
* `ssh`
* `dd`
* `bash`
* `sudo`
* `lsblk` or `diskutil`

## Usage

Install and setup a new project:

```
git clone git@github.com:fatehitech/beaglebench ~/.beaglebench
mkdir my-bench && cd my-bench
cat <<EOF > bb
#!/bin/bash
python ~/.beaglebench/bench.py $@
EOF
chmod a+x bb
```

## Features

It can create an SD card for your beaglebone:

`./bb sd` fetches, checksums, and writes the official debian OS image onto your SD card.

Now that you have an SD card, pop it into the BeagleBone and plug in with USB. The USB network feature allows beaglebench to do much more.

It can assist you in the development and testing of alterations to the running beaglebone:

`./bb setup` runs all the *.sh scripts in ./setup as though they were on the machine. this is a convenient way to make simple changes to the environment as though you were ssh'd in. Anything exiting non-zero will throw an error. You should write these in an idempotent way for best results.

`./bb reboot` gracefully reboot the beaglebone.

`./bb test` runs all the *.sh scripts in ./test as though they were on the machine. This is where you will want to verify that things have been setup correctly. You should run this after setup and after reboot. Anything exiting non-zero will throw an error

For more options and additional information, execute `./bb` for help.

Here is the in-app help:

```
Help on class Commands in module BeagleBench CLI:

class Commands
 |  Commands are implemented as methods in this object
 |
 |  Some commands may take arguments.
 |  E.g. If you know your SD card is on /dev/sdb you could go
 |      ./bb sd /dev/sdb
 |  and /dev/sdb will be passed in as the device_node
 |
 |  Any communication with the BeagleBone is via SSH by means of the USB network
 |
 |  Add more functionality by editing /Users/keyvan/.beaglebench/bench.py
 |
 |  Methods defined here:
 |
 |  reboot(self)
 |      Reboot the BeagleBone
 |
 |  sd(self, device_node=None)
 |      Interactively prepare an SD card
 |
 |  setup(self)
 |      Transfer and run all setup scripts on the BeagleBone
 |
 |  test(self)
 |      Transfer and run all test scripts on the BeagleBone
```

## Variables and Skipping

You can add a file `vars.sh` to your directory and define variables here. This file is sourced into the local and remote environment and so the variables defined here are available in your setup and test scripts.

You may want to skip some scripts. For example if you have scripts `setup/my-long-setup.sh` and `test/my-long-test.sh` you can skip them by defining a special variable `skip` in `vars.sh` like so:

```bash
skip=(
  "setup/my-long-setup.sh"
  "test/my-long-test.sh"
)
```

This way, these two scripts will be skipped during remote execution.
