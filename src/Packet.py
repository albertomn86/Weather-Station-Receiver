from PayloadDecoder import PayloadDecoder


class Packet(object):

    def __init__(self, frame):
        self.type = frame[0]
        self.deviceId = frame[1:5]
        self.payload = PayloadDecoder.Decode(frame[5:])
