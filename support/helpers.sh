function remotely_run_scripts_in() {
scripts_dir=$1

if [[ ! -d $scripts_dir ]]; then
  echo "ERROR: no such directory $scripts_dir"
  exit 1
fi

script=/tmp/script
echo "set -e # Exit on error" > $script
if [[ -f config_vars.sh ]]; then
  echo "$(cat config_vars.sh)" > $script
fi

script_listing=$(ls $scripts_dir)
script_paths=( $script_listing )

for child_script in $script_paths
do
  child_script_path=$scripts_dir/$child_script
  content=$(cat $child_script_path)
  echo "echo 'Running $child_script_path'" >> $script
  echo "$content" >> $script
done

cat $script | ssh -o ConnectTimeout=1 -o LogLevel=Error $BEAGLEBONE_USER@$BEAGLEBONE_HOST bash

return $?
}
