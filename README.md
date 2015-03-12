# BeagleStrap

This is a set of bash scripts driven by a simple Makefile.

The first thing you should do is get the beaglebone running. You'll need an SD card.

`make sd` fetches, checksums, and writes an upstream OS image onto your SD card. you can change the desired image in `Image/config.sh`

Now that you have an SD card, pop it into the BeagleBone and plug in with USB. Everything else runs over the USB network.

`make setup` runs all the scripts in SetupScripts as though they were on the machine. this is a convenient way to make simple changes to the environment as though you were ssh'd in. anything exiting non-zero will throw an error.

`make test` runs all the scripts in TestScripts exactly like make setup. unlike the setup scripts, these scripts should only verify. anything exiting non-zero will throw an error


