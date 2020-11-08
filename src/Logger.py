class Logger(object):

    def __init__(self):
        self.lastMessage = ""

    def Write(self, message):
        self.lastMessage = message
