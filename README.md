# beaglebench

Beaglebench provides a python-based task runner for people who work with the BeagleBone. It gives you a simple way to create SD cards and perform post-install configuration and testing.

By running scripts from a pristine, official image, you can iterate more rapidly than if you were creating custom images. In addition, if you write your scripts in an idempotent way (same script can be run over and over, on the same machine, without consequence), you have a repeatable recipe for performing these customizations while maintaining a tight feedback loop.

I've found this to be my favorite workflow so far that I've been trying to figuring out how to work with the beaglebone in a consistent, more rigorous manner.

# Requirements

Linux or Mac

These programs must be available on your workbench machine:

* python
* curl
* ssh
* dd
* unxz
* lsblk (diskutil will be used on mac)
* git
* bash
* sudo

## Usage

Install and setup a new project:

```
git clone git@github.com:fatehitech/beaglebench ~/.beaglebench
mkdir my-bench
cd my-bench
ln -s ~/.beaglebench/bench.py bb
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
 |  These are all the commands avaiable to you.
 |  
 |  Some commands can take optional arguments.
 |  E.g. If you know your SD card is on /dev/sdb you could go
 |      ./bb sd /dev/sdb
 |  and /dev/sdb will be passed in as the device_node
 |  
 |  Any communication with the BeagleBone is via SSH by means of the USB network
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
