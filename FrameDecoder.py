from Packet import Packet

class FrameDecoder(object):

    def __init__(self, frame):
        if self.IsValid(frame):
            self._frame = frame
        else:
            raise ValueError("Invalid frame {0}".format(frame))


    @staticmethod
    def IsValid(testFrame):
        if len(testFrame) <= 6:
            return False

        if not testFrame.endswith('#'):
            return False

        if not (testFrame.startswith('S') or testFrame.startswith('K')):
            return False

        return True


    def GetPacket(self):
        packet = Packet()
        packet.Type = self._frame[0]
        packet.From = self._frame[1:5]
        packet.Payload = self._frame[5:-1]

        return packet
