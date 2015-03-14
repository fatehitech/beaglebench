# beaglebench

Beaglebench provides a python-based task runner for people who work with the BeagleBone. It gives you a simple way to create SD cards and perform post-install configuration and testing.

By running scripts from a pristine, official image, you can iterate more rapidly than if you were creating custom images. In addition, if you write your scripts in an idempotent way (same script can be run over and over, on the same machine, without consequence), you have a repeatable recipe for performing these customizations while maintaining a tight feedback loop.

I've found this to be my favorite workflow so far that I've been trying to figuring out how to work with the beaglebone in a consistent, more rigorous manner.

# Requirements

These programs must be available on your workbench machine:

* python
* curl
* ssh
* dd
* unxz
* lsblk
* md5sum
* git
* bash
* sudo

## Usage

Create a new beaglebench project:

```
mkdir my-bench
cd my-bench
curl -o bb https://raw.githubusercontent.com/fatehitech/beaglebench/master/bench.py
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
