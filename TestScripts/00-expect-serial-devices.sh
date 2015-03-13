for n in 0 2
do
  tty=/dev/ttyO$n
  echo -n "Checking existence of $tty ... "
  if test -c $tty; then
    echo "OK"
  else
    echo "ERROR: $tty does not exist"
    exit 1
  fi
done
