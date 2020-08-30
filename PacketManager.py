from Packet import Packet
from Config import Config

class PacketManager(object):

    def __init__(self):
        self._config = Config("Config_test.yml")

    def __init__(self, config):
        self._config = config

    def Decode(self, packet):
        if not packet.From in self._config.GetDevices():
            raise ValueError("Packet from not registered device")
