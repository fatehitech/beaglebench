import os, stat, repo, hashlib, block_device, bincache
import platform_specific as helpers
from subprocess import call, check_output

def make(device_node):
    cache = os.path.join(repo.root, 'cache', 'images')
    baseURL = "https://rcn-ee.net/rootfs/bb.org/release/2015-03-01/lxde-4gb"
    image_name = "bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb"
    archive_checksum = "c848627722b7a5f7bc89791cc8949e3b"
    img = cache+"/"+image_name+".img"
    archive_name = image_name+".img.xz"
    archive = cache+"/"+archive_name
    archive_url = baseURL+"/"+archive_name
    if bincache.file_exists(img): return interactive_write(img, device_node)
    if bincache.file_exists(archive) and bincache.checksum_match(archive, archive_checksum):
        extract_archive(archive)
    else:
        bincache.download(archive_url, archive)
    make(device_node)

def extract_archive(fp):
    print "Extracting "+fp
    call(['unxz', fp]);

def interactive_write(fp, node=""):
    node = block_device.select(node)
    prompt = "Will completely erase %s -- continue? (y/N): " % node
    response = raw_input(prompt).strip()
    if len(response) > 0 and response[0] is "y": write_image(fp, node)
    else: print "Bailing"
    
def write_image(fp, node):
    call(['sudo', 'dd', 'if='+fp, 'of='+node, 'bs=1M'])
