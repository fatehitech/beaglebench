for n in 0 1 2
do
  tty=/dev/ttyO$n
  echo -n "Checking $tty ... "
  if test -c $tty; then
    echo "OK"
  else
    echo "ERROR"
    exit 1
  fi
done
