echo -n "Checking that UART0 is not in use by getty ... "
if [[ `ps aux | grep [t]tyO0` ]]; then
  echo "ERROR"
  exit 1
else
  echo "OK"
fi
