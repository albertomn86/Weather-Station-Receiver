from time import sleep
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    pass


at_pin = 11


class Radio(object):

    def __init__(self, socket):
        self.socket = socket

    def config(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(at_pin, GPIO.OUT)

        self.__set_power(6)
        self.__set_channel("001")
        self.__set_mode("FU1")

        GPIO.cleanup()

    def __send_at_command(self, command):
        GPIO.output(at_pin, GPIO.LOW)
        self.socket.send_frame(command)
        GPIO.output(at_pin, GPIO.HIGH)
        sleep(0.1)

    def __set_power(self, power):
        self.__send_at_command(f"AT+P{str(power)}")

    def __set_channel(self, channel):
        self.__send_at_command(f"AT+C{channel}")

    def __set_mode(self, mode):
        self.__send_at_command(f"AT+{mode}")
