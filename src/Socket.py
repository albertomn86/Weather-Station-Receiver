import serial


class Socket(object):

    def __init__(self, serialPort="/dev/ttyS0"):
        self.socket = serial.Serial(
            port=serialPort,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def ReadFrame(self):
        return self.socket.readline()
