
class PacketReceiver(object):

    @staticmethod
    def IsValid(packet):

        if not packet.endswith('#'):
            return False

        if not packet.split(';')[0] in ("S0", "S1", "R0"):
            return False

        return True
