from pytest import raises
from PayloadDecoder import PayloadDecoder


def test_payload_must_fail_if_contains_an_invalid_element():
    raw_payload = "4FD0"

    with raises(ValueError, match=r"Payload not valid: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_fail_with_invalid_temperature():
    raw_payload = "T10000"

    with raises(ValueError, match=r"Invalid temperature value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_temperature():
    raw_payload = "T2226"

    payload = PayloadDecoder.decode(raw_payload)

    assert 22.26 == payload.temperature


def test_payload_must_decode_valid_negative_temperature():
    raw_payload = "T-510"

    payload = PayloadDecoder.decode(raw_payload)

    assert -5.10 == payload.temperature


def test_payload_must_fail_with_humidity_greather_than_100():
    raw_payload = "H10100"

    with raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_fail_with_humidity_lower_than_0():
    raw_payload = "H-100"

    with raises(ValueError, match=r"Invalid humidity value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_humidity():
    raw_payload = "H4510"

    payload = PayloadDecoder.decode(raw_payload)

    assert 45.10 == payload.humidity


def test_payload_must_fail_with_luminosity_lower_than_0():
    raw_payload = "L-1"

    with raises(ValueError, match=r"Invalid luminosity value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_luminosity():
    raw_payload = "L500000"

    payload = PayloadDecoder.decode(raw_payload)

    assert 5000.0 == payload.luminosity


def test_payload_must_fail_with_invalid_status():
    raw_payload = "S32"

    with raises(ValueError, match=r"Invalid status value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_status():
    raw_payload = "S8"

    payload = PayloadDecoder.decode(raw_payload)

    assert 8 == payload.status


def test_payload_must_fail_with_invalid_battery():
    raw_payload = "B-100"

    with raises(ValueError, match=r"Invalid battery voltage value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_battery():
    raw_payload = "B412"

    payload = PayloadDecoder.decode(raw_payload)

    assert 4.12 == payload.battery


def test_payload_must_fail_with_invalid_interval():
    raw_payload = "I0"

    with raises(ValueError, match=r"Invalid interval value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_interval():
    raw_payload = "I300"

    payload = PayloadDecoder.decode(raw_payload)

    assert 300 == payload.interval


def test_payload_must_fail_with_invalid_uv_radiation():
    raw_payload = "U-100"

    with raises(ValueError, match=r"Invalid UV radiation value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_uv_radiation():
    raw_payload = "U856"

    payload = PayloadDecoder.decode(raw_payload)

    assert 8.56 == payload.uv_radiation


def test_payload_must_fail_with_invalid_pressure():
    raw_payload = "P79912"

    with raises(ValueError, match=r"Invalid pressure value: .*"):
        PayloadDecoder.decode(raw_payload)


def test_payload_must_decode_valid_pressure():
    raw_payload = "P101812"

    payload = PayloadDecoder.decode(raw_payload)

    assert 1018.12 == payload.pressure


def test_payload_must_decode_valid_packet_with_all_data():
    raw_payload = "P101812;T-304;H8000;S12;I300;L300000;B419"

    payload = PayloadDecoder.decode(raw_payload)

    assert -3.04 == payload.temperature
    assert 80.00 == payload.humidity
    assert 1018.12 == payload.pressure
    assert 300 == payload.interval
    assert 12 == payload.status
    assert payload.uv_radiation is None
    assert 4.19 == payload.battery
    assert 3000.0 == payload.luminosity
