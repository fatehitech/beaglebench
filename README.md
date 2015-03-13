# beaglebench

Beaglebench is a folder structure, a few scripts, and a couple of patterns that together help organize and perform common tasks related to the Beaglebone.

## Usage

Clone it down and being customizing

## Features

It can create an SD card for your beaglebone:

`make sd` fetches, checksums, and writes an upstream OS image onto your SD card. you can change the desired image in `Image/config.sh`

Now that you have an SD card, pop it into the BeagleBone and plug in with USB. The USB network feature allows beaglebench to do much more.

It can assist you in the development and testing of alterations to the running beaglebone:

`make setup` runs all the scripts in SetupScripts as though they were on the machine. this is a convenient way to make simple changes to the environment as though you were ssh'd in. anything exiting non-zero will throw an error.

`make test` runs all the scripts in TestScripts exactly like make setup. unlike the setup scripts, these scripts should only verify. anything exiting non-zero will throw an error
