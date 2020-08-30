from pytest import raises
from Packet import Packet
from Config import Config
from PacketManager import PacketManager


config = Config("Tests/Config_test.yml")


def test_ValifPacketFromNotRegisteredDeviceMustBeRejected():

    validFrame = "S80D34FD0"
    packet = Packet(validFrame)
    packetManager = PacketManager(config)

    with raises(ValueError, match=r"Packet from not registered device"):
        packetManager.Decode(packet)
