# beaglebench

Beaglebench is a folder structure, a few scripts, and a couple of patterns that together help organize and perform common tasks related to the Beaglebone.

# Requirements

* python
* curl
* git

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

`./bb sd` fetches, checksums, and writes an upstream OS image onto your SD card. you can change the desired image in `Image/config.sh`

Now that you have an SD card, pop it into the BeagleBone and plug in with USB. The USB network feature allows beaglebench to do much more.

It can assist you in the development and testing of alterations to the running beaglebone:

`./bb setup` runs all the scripts in SetupScripts as though they were on the machine. this is a convenient way to make simple changes to the environment as though you were ssh'd in. anything exiting non-zero will throw an error.

`./bb test` runs all the scripts in TestScripts exactly like make setup. unlike the setup scripts, these scripts should only verify. anything exiting non-zero will throw an error
