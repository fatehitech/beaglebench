function run_scripts_in() {

scripts=$1

if [[ ! -d $1 ]]; then
  echo "You must pass in a directory"
  exit 1
fi


script=/tmp/script
cat <<EOF > $script
set -e # Exit on error
EOF

for part in $(ls $scripts)
do
spath=$scripts/$part
content=$(cat $spath)
cat <<EOF >> $script
echo "Running $part"
$content
EOF
done

cat $script | ssh -o LogLevel=Error root@192.168.7.2 bash

return $?

}
