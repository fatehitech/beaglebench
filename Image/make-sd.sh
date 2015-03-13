#!/bin/bash
source Image/writer.sh
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
