cat <<PYTHON | python
import serial

UART0 = serial.Serial('/dev/ttyO0',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0)

UART2 = serial.Serial('/dev/ttyO2',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0)

# UART2 is chained to UART0
# UART0 is chained to UART2

UART2.write("hello")
assert UART0.read(64) == "hello", "expected data written to UART2 to be readable on UART0"

UART0.write("goodbye")
assert UART2.read(64) == "goodbye", "expected data written to UART0 to be readable on UART2"
PYTHON
