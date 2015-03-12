write_image() {
  img_path=$1
  if [[ ! -f $img_path ]]; then 
    echo "Invalid image path"; exit 1;
  fi
  lsblk
  echo -n "Which one is the SD card? (e.g. /dev/sdb): "
  read DISK
  echo "Will completely erase ${DISK} -- CTRL-C to cancel, otherwise hit any key"
  read
  echo "Writing $img_path to ${DISK}"
  sudo dd if=$img_path of=${DISK} bs=1M
}
