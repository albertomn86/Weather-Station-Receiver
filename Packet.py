
class Packet(object):

    def __init__(self, frame):
        self.Type = frame[0]
        self.From = frame[1:5]
        self.Payload = frame[5:]
