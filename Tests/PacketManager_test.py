from sys import path as sysPath
from os import path as osPath
sysPath.append(osPath.abspath("./"))
from Packet import Packet
from Config import Config
from PacketManager import PacketManager
import pytest


config = Config("Tests/Config_test.yml")

def test_ValifPacketFromNotRegisteredDeviceMustBeRejected():

    validFrame = "S80D34FD0"
    packet = Packet(validFrame)
    packetManager = PacketManager(config)

    with pytest.raises(ValueError, match=r"Packet from not registered device"):
        packetManager.Decode(packet)
