from pytest import raises
from Packet import Packet
from Config import Config
from PacketManager import PacketManager
from os import path, remove


config = Config("Tests/ConfigurationFiles/Config_test.yml")


def test_ValifPacketFromNotRegisteredDeviceMustBeRejected():

    validFrame = "S80D3P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(validFrame)
    packetManager = PacketManager(config)

    with raises(ValueError, match=r"Packet from unregistered device"):
        packetManager.ProcessPacket(packet)


def test_DecodeMustReturnJSONStringWithValidPacket():

    validFrame = "S80D4P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(validFrame)
    packetManager = PacketManager(config)

    ts = 1598892487509
    decoded = packetManager.ProcessPacket(packet, ts)

    expected = r'{"ts": 1598892487509, "values": {"battery": 4.19, ' \
        + r'"deviceId": "80D4", "humidity": 80.0, "interval": 300, ' \
        + r'"luminosity": 3000, "pressure": 1018.12, "status": 12, ' \
        + r'"temperature": -3.04, "uvRadiation": 0.67}}'
    assert expected == decoded


def test_WhenADeviceHasSubscribedDevicesTheLastPayloadMustBeStored():

    validFrame = "S80D4P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(validFrame)
    packetManager = PacketManager(config)

    packetManager.ProcessPacket(packet)

    tmpFile = "80D4.tmp"
    found = path.exists(tmpFile)

    remove(tmpFile)

    assert found


def test_WhenADeviceHasNotSubscribedDevicesTheMustNotBeStored():

    validFrame = "SA3F6P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(validFrame)
    packetManager = PacketManager(config)

    packetManager.ProcessPacket(packet)

    tmpFile = "A3F6.tmp"
    found = path.exists(tmpFile)

    assert not found
