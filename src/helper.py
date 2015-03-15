import os, repo, subprocess

try: bb_user = os.environ['BEAGLEBONE_USER']
except Exception: bb_user = 'root'

try: bb_host = os.environ['BEAGLEBONE_HOST']
except Exception: bb_host = '192.168.7.2'

env = { 'BEAGLEBONE_USER': bb_user,
        'BEAGLEBONE_HOST': bb_host }

def call(helper_string):
    cmd = 'source '+repo.helpers+' && '+helper_string
    return subprocess.call(['bash', '-c', cmd], env=env)
