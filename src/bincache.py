import os, repo, hashlib
from distutils import dir_util
from subprocess import call

cache = os.path.join(repo.root, 'cache', 'binaries')

def needs(url, filename, checksum):
    localpath = cache+'/'+filename
    if file_exists(localpath) and checksum_match(localpath, checksum):
        return localpath
    else:
        download(url, localpath)
        return needs(url, filename, checksum)

def download(url, filepath):
    dir_util.mkpath(os.path.dirname(filepath))
    call(['curl', '-o', filepath, url])

def md5sum(fp, block_size=2**20):
    f = open(fp, 'rb')
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def checksum_match(fp, expected):
    return md5sum(fp) == expected

def file_exists(path):
    return os.path.isfile(path)
