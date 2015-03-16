containsElement () {
  local e
  for e in "${@:2}"; do [[ "$e" == "$1" ]] && return 0; done
  return 1
}

function ssh_beaglebone() {
ssh \
  -o LogLevel=Error \
  -o ConnectTimeout=1 \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null \
  $BEAGLEBONE_USER@$BEAGLEBONE_HOST $@
}

function reboot_beaglebone() {
ssh_beaglebone reboot
}

function remotely_run_scripts_in() {
scripts_dir=$1

if [[ ! -d $scripts_dir ]]; then
  echo "ERROR: no such directory $scripts_dir"
  exit 1
fi

script=/tmp/script
echo "set -e # Exit on error" > $script

skip=()
if [[ -f vars.sh ]]; then
  echo "$(cat vars.sh)" > $script
  source vars.sh
fi

script_listing=$(ls $scripts_dir)

for child_script in $script_listing
do
  child_script_path=$scripts_dir/$child_script
  containsElement "$child_script_path" "${skip[@]}"
  if [[ "$?" = "0" ]]; then
    echo "Skipping $child_script"
  else
    content=$(cat $child_script_path)
    echo "echo 'Running $child_script_path'" >> $script
    echo "$content" >> $script
  fi
done

cat $script | ssh_beaglebone bash

return $?
}
