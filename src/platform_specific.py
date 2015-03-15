from sys import platform as _platform
from subprocess import call

if _platform == "linux" or _platform == "linux2":
  def listBlockDevices():
    print "Here's the output of `lsblk`"
    call(['lsblk'])
elif _platform == "darwin":
  def listBlockDevices():
    print "Here's the output of `diskutil list`"
    call(['diskutil', 'list'])
    print "You are on a mac! Use /dev/rdisk* instead of /dev/disk* for a much faster copy process."
elif _platform == "win32":
  pass

