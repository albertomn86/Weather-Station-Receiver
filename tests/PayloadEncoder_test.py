from PayloadEncoder import PayloadEncoder
from Payload import Payload


def test_given_an_one_element_payload_must_return_string():
    payload = Payload()
    payload.humidity = 77.0

    generated = PayloadEncoder.encode(payload)

    assert "H7700" == generated


def test_given_two_elements_payload_must_return_string():
    payload = Payload()
    payload.uv_radiation = 0.01
    payload.temperature = -1.01

    generated = PayloadEncoder.encode(payload)

    assert "T-101;U001" == generated


def test_given_full_payload_must_return_full_string():
    payload = Payload()
    payload.uv_radiation = 3.22
    payload.temperature = -1.0
    payload.interval = 300
    payload.luminosity = 5000.0
    payload.pressure = 1080.03
    payload.humidity = 40.0
    payload.status = 0
    payload.battery = 4.11

    generated = PayloadEncoder.encode(payload)

    assert "B411;H4000;I300;L500000;P108003;S0;T-100;U322" == generated
