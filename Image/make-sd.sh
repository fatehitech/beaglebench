#!/bin/bash
source Image/config.sh
source Image/writer.sh
img="Image/$image_name.img"
archive_name="$image_name.img.xz"
archive="Image/$archive_name"
archive_url="$image_remote_root/$archive_name"
if [[ -f $img ]]; then
  write_image $img
elif [[ -f $archive ]]; then
  checksum $archive
  #unxz $archive
  #write_image $img
else
  curl -o $archive $archive_url
  checksum $archive
fi
#	wget 
#	md5sum: 7db9e848f4853bbab51a3466e9fce9f5
