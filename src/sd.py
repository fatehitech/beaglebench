import os, stat
from distutils import dir_util
from subprocess import call, check_output

def make(device_node):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    cache = os.path.join(root, 'cache', 'images')
    baseURL = "https://rcn-ee.net/rootfs/bb.org/release/2015-03-01/lxde-4gb"
    image_name = "bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb"
    archive_checksum = "c848627722b7a5f7bc89791cc8949e3b"
    img = cache+"/"+image_name+".img"
    archive_name = image_name+".img.xz"
    archive = cache+"/"+archive_name
    archive_url = baseURL+"/"+archive_name
    if file_exists(img): return interactive_write(img, device_node)
    if file_exists(archive) and checksum_match(archive, archive_checksum):
        extract_archive(archive)
    else:
        download_archive(archive_url, archive)
    make()

def file_exists(path):
    return os.path.isfile(path)

def checksum_match(fp, expected):
    print "Verifying "+fp
    return check_output(['md5sum', fp]).split(' ')[0] == expected

def download_archive(url, filepath):
    dir_util.mkpath(os.path.dirname(filepath))
    call(['curl', '-o', filepath, url])

def extract_archive(fp):
    print "Extracting "+fp
    call(['unxz', fp]);

def is_block_device(filename):
    if not filename: return False
    try:
        mode = os.lstat(filename).st_mode
    except OSError:
        return False
    else:
        return stat.S_ISBLK(mode)

def interactive_write(fp, node=""):
    print "Here's the output of lsblk"
    call(['lsblk'])
    prompt = "Enter the top-level device path of SD card (e.g. /dev/sdb): "
    while not is_block_device(node): node = raw_input(prompt).strip()
    prompt = "Will completely erase %s -- continue? (y/N): " % node
    response = raw_input(prompt).strip()
    if len(response) > 0 and response[0] is "y": write_image(fp, node)
    else: print "Bailing"
    
def write_image(fp, node):
    call(['sudo', 'dd', 'if='+fp, 'of='+node, 'bs=1M'])
