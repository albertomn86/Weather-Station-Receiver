import datetime
import socket


class Logger(object):

    WARN = "WARNING"
    ERR = "ERROR"
    INFO = "INFO"

    def __init__(self, outputEnabled=False):
        self.lastMessage = ""
        self.output = outputEnabled

    def Write(self, msgType, message):
        self.lastMessage = message
        if self.output:
            print(self.FormatOutput(msgType, message))

    @staticmethod
    def FormatOutput(msgType, message):
        timeNow = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
        hostname = socket.gethostname()
        output = f"{timeNow} {hostname} WS-Receiver: ({msgType}) {message}"
        return output
