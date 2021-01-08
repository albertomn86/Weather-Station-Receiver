from Device import Device
from pytest import raises


def test_given_a_raw_device_must_convert_id_to_uppercase():
    raw = {"ID": "a3f6"}
    device = Device(raw)

    assert device.id == "A3F6"


def test_given_a_raw_device_with_invalid_id_must_raise_exception():
    raw = {"ID": "a"}

    with raises(ValueError, match=r"Invalid ID"):
        Device(raw)


def test_given_a_raw_device_without_id_must_raise_exception():
    raw = {"Interval": 300}

    with raises(ValueError, match=r"Invalid ID"):
        Device(raw)


def test_given_a_raw_device_must_parse_interval_lower_than_60():
    raw = {"ID": "A3F6", "Interval": 3}
    device = Device(raw)

    assert device.interval == 60


def test_given_a_raw_device_must_parse_altitude_greather_than_0():
    raw = {"ID": "A3F6", "Altitude": 848}
    device = Device(raw)

    assert device.altitude == 848


def test_given_a_raw_device_must_parse_altitude_lower_than_0():
    raw = {"ID": "A3F6", "Altitude": -1}
    device = Device(raw)

    assert device.altitude == 0


def test_given_a_raw_device_without_subscription_must_return_default():
    raw = {"ID": "a3f6", "Interval": 300}
    device = Device(raw)

    assert ['I'] == device.subscriptionValues


def test_given_a_raw_device_must_return_ordered_subscription_list():
    raw = {
            "ID": "a3f6",
            "Subscription":
            {
                "Values": "T,h,P,U,l ,B",
                "Device": "A3F6"
            },
            "Interval": 300
        }
    device = Device(raw)

    assert ['B', 'H', 'I', 'L', 'P', 'T', 'U'] == device.subscriptionValues
    assert "A3F6" == device.subscriptionDevice


def test_given_a_raw_device_with_an_invalid_value_must_raise_exception():
    raw = {
            "ID": "a3f6",
            "Subscription":
            {
                "Values": "T,h,P,U,l,B,C",
                "Device": "A3F6"
            },
            "Interval": 300
        }

    with raises(ValueError, match=r"Invalid subscription value: 'C'"):
        Device(raw)


def test_given_a_raw_device_without_subscription_must_raise_exception():
    raw = {
        "ID": "a3f6",
        "Subscription":
        {
            "Values": "T,h,P,U,l,B"
        },
        "Interval": 300
    }

    with raises(ValueError, match=r"Subscription device not found"):
        Device(raw)
