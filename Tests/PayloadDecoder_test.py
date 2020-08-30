from pytest import raises
from PayloadDecoder import PayloadDecoder
from Packet import Packet


def test_PayloadMustFailIContainsAnInvalidElement():
    validFrame = "S80D34FD0"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Payload not valid: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustFailWithInvalidTemperature():
    validFrame = "S80D3T10000"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid temperature value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidTemperature():
    validFrame = "S80D3T2226"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 22.26 == payload.temperature


def test_PayloadMustDecodeValidNegativeTemperature():
    validFrame = "S80D3T-510"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert -5.10 == payload.temperature


def test_PayloadMustFailWithHumidityGreatherThan100():
    validFrame = "S80D3H10100"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustFailWithHumidityLowerThan0():
    validFrame = "S80D3H-100"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidHumidity():
    validFrame = "S80D3H4510"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 45.10 == payload.humidity


def test_PayloadMustFailWithLuminosityLowerThan0():
    validFrame = "S80D3L-1"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid luminosity value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidLuminosity():
    validFrame = "S80D3L5000"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 5000 == payload.luminosity


def test_PayloadMustFailWithInvalidStatus():
    validFrame = "S80D3S32"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid status value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidStatus():
    validFrame = "S80D3S8"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 8 == payload.status


def test_PayloadMustFailWithInvalidBattery():
    validFrame = "S80D3B-100"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid battery voltage value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidBattery():
    validFrame = "S80D3B412"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 4.12 == payload.battery


def test_PayloadMustFailWithInvalidInterval():
    validFrame = "S80D3I0"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid interval value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidInterval():
    validFrame = "S80D3I300"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 300 == payload.interval


def test_PayloadMustFailWithInvalidUVRadiation():
    validFrame = "S80D3U-100"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid UV radiation value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidUVRadiation():
    validFrame = "S80D3U856"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 8.56 == payload.uvRadiation


def test_PayloadMustFailWithInvalidPressure():
    validFrame = "S80D3P79912"
    packet = Packet(validFrame)

    with raises(ValueError, match=r"Invalid pressure value: .*"):
        PayloadDecoder.DecodeFromPacket(packet)


def test_PayloadMustDecodeValidPressure():
    validFrame = "S80D3P101812"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert 1018.12 == payload.pressure


def test_PayloadMustDecodeValidPacketWithAllData():
    validFrame = "S80D3P101812;T-304;H8000;S12;I300;L3000;B419"
    packet = Packet(validFrame)

    payload = PayloadDecoder.DecodeFromPacket(packet)

    assert -3.04 == payload.temperature
    assert 80.00 == payload.humidity
    assert 1018.12 == payload.pressure
    assert 300 == payload.interval
    assert 12 == payload.status
    assert payload.uvRadiation is None
    assert 4.19 == payload.battery
    assert 3000 == payload.luminosity
