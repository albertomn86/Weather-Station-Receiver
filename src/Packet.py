from src.PayloadDecoder import PayloadDecoder


class Packet(object):

    def __init__(self, frame: str):
        self.type = frame[0]
        self.device_id = frame[1:5]
        self.payload = PayloadDecoder.decode(frame[5:])
