import datetime
import socket


class Logger(object):

    WARN = "WARNING"
    ERR = "ERROR"
    INFO = "INFO"

    def __init__(self, output_enabled=False):
        self.last_message = ""
        self.__output = output_enabled

    def write(self, msg_type, message):
        self.last_message = message
        if self.__output:
            print(Logger.format_output(msg_type, message))

    @staticmethod
    def format_output(msg_type, message):
        timenow = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
        hostname = socket.gethostname()
        output = f"{timenow} {hostname} WS-Receiver: ({msg_type}) {message}"
        return output
