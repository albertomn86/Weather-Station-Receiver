from pytest import raises
from PayloadDecoder import PayloadDecoder


def test_PayloadMustFailIContainsAnInvalidElement():
    rawPayload = "4FD0"

    with raises(ValueError, match=r"Payload not valid: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustFailWithInvalidTemperature():
    rawPayload = "T10000"

    with raises(ValueError, match=r"Invalid temperature value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidTemperature():
    rawPayload = "T2226"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 22.26 == payload.temperature


def test_PayloadMustDecodeValidNegativeTemperature():
    rawPayload = "T-510"

    payload = PayloadDecoder.Decode(rawPayload)

    assert -5.10 == payload.temperature


def test_PayloadMustFailWithHumidityGreatherThan100():
    rawPayload = "H10100"

    with raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustFailWithHumidityLowerThan0():
    rawPayload = "H-100"

    with raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidHumidity():
    rawPayload = "H4510"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 45.10 == payload.humidity


def test_PayloadMustFailWithLuminosityLowerThan0():
    rawPayload = "L-1"

    with raises(ValueError, match=r"Invalid luminosity value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidLuminosity():
    rawPayload = "L500000"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 5000.0 == payload.luminosity


def test_PayloadMustFailWithInvalidStatus():
    rawPayload = "S32"

    with raises(ValueError, match=r"Invalid status value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidStatus():
    rawPayload = "S8"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 8 == payload.status


def test_PayloadMustFailWithInvalidBattery():
    rawPayload = "B-100"

    with raises(ValueError, match=r"Invalid battery voltage value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidBattery():
    rawPayload = "B412"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 4.12 == payload.battery


def test_PayloadMustFailWithInvalidInterval():
    rawPayload = "I0"

    with raises(ValueError, match=r"Invalid interval value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidInterval():
    rawPayload = "I300"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 300 == payload.interval


def test_PayloadMustFailWithInvalidUVRadiation():
    rawPayload = "U-100"

    with raises(ValueError, match=r"Invalid UV radiation value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidUVRadiation():
    rawPayload = "U856"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 8.56 == payload.uvRadiation


def test_PayloadMustFailWithInvalidPressure():
    rawPayload = "P79912"

    with raises(ValueError, match=r"Invalid pressure value: .*"):
        PayloadDecoder.Decode(rawPayload)


def test_PayloadMustDecodeValidPressure():
    rawPayload = "P101812"

    payload = PayloadDecoder.Decode(rawPayload)

    assert 1018.12 == payload.pressure


def test_PayloadMustDecodeValidPacketWithAllData():
    rawPayload = "P101812;T-304;H8000;S12;I300;L300000;B419"

    payload = PayloadDecoder.Decode(rawPayload)

    assert -3.04 == payload.temperature
    assert 80.00 == payload.humidity
    assert 1018.12 == payload.pressure
    assert 300 == payload.interval
    assert 12 == payload.status
    assert payload.uvRadiation is None
    assert 4.19 == payload.battery
    assert 3000.0 == payload.luminosity
