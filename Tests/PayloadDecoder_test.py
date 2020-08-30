from sys import path as sysPath
from os import path as osPath
sysPath.append(osPath.abspath("./"))
from PayloadDecoder import PayloadDecoder
from Packet import Packet
import pytest


def test_PayloadMustFailIContainsAnInvalidElement():
    validFrame = "S80D34FD0"
    packet = Packet(validFrame)

    with pytest.raises(ValueError, match=r"Payload not valid: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustFailWithInvalidTemperature():
    validFrame = "S80D3T10000"
    packet = Packet(validFrame)

    with pytest.raises(ValueError, match=r"Invalid temperature value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidTemperature():
    validFrame = "S80D3T2226"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 22.26 == payload.temperature


def test_PayloadMustFailWithHumidityGreatherThan100():
    validFrame = "S80D3H10100"
    packet = Packet(validFrame)

    with pytest.raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustFailWithHumidityLowerThan0():
    validFrame = "S80D3H-100"
    packet = Packet(validFrame)

    with pytest.raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidHumidity():
    validFrame = "S80D3H4510"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 45.10 == payload.humidity
