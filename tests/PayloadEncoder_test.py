from PayloadEncoder import PayloadEncoder
from Payload import Payload


def test_GivenAnOneElementPayloadMustReturnString():
    payload = Payload()
    payload.humidity = 77.0

    generated = PayloadEncoder.Encode(payload)

    assert "H7700" == generated


def test_GivenTwoElementsPayloadMustReturnString():
    payload = Payload()
    payload.uvRadiation = 0.01
    payload.temperature = -1.01

    generated = PayloadEncoder.Encode(payload)

    assert "T-101;U001" == generated


def test_GivenFullPayloadMustReturnFullString():
    payload = Payload()
    payload.uvRadiation = 3.22
    payload.temperature = -1.0
    payload.interval = 300
    payload.luminosity = 5000.0
    payload.pressure = 1080.03
    payload.humidity = 40.0
    payload.status = 0
    payload.battery = 4.11

    generated = PayloadEncoder.Encode(payload)

    assert "B411;H4000;I300;L500000;P108003;S0;T-100;U322" == generated
