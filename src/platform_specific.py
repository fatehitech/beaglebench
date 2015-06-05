import sys
from subprocess import call, check_output
_platform = sys.platform

if _platform == "linux" or _platform == "linux2":
  def listBlockDevices():
    print2("Here's the output of `lsblk`")
    print2(check_output(['lsblk']))
elif _platform == "darwin":
  def listBlockDevices():
    print2("Here's the output of `diskutil list`")
    print2(check_output(['diskutil', 'list']))
elif _platform == "win32":
  pass

def write2(txt):
    sys.stderr.write(txt);


def print2(txt):
    write2(txt+'\n')
