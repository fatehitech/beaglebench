import os
join = os.path.join


def make():
    here = os.getcwd()
    baseURL = "https://rcn-ee.net/rootfs/bb.org/release/2015-03-01/lxde-4gb"
    image_name = "bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb"
    archive_checksum = "c848627722b7a5f7bc89791cc8949e3b"
    img = here+"/Image/"+image_name+".img"
    archive_name = image_name+".img.xz"
    archive = here+"/Image/"+archive_name
    archive_url = baseURL+"/"+archive_name
    print "ok"
