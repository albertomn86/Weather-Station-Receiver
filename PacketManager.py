from Config import Config


class PacketManager(object):

    def __init__(self, config=Config("Config.yml")):
        self._config = config

    def Decode(self, packet):
        if packet.From not in self._config.GetDevices():
            raise ValueError("Packet from not registered device")
