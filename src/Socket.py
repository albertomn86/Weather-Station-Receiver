import serial


class Socket(object):

    def __init__(self, serial_port="/dev/ttyS0"):
        self._socket = serial.Serial(
            port=serial_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def read_frame(self):
        return self._socket.readline().decode()

    def send_frame(self, frame):
        self._socket.write(frame.encode())
