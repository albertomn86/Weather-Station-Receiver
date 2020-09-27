from Device import Device
from pytest import raises


def test_GivenARawDeviceMustConvertIdToUppercase():
    raw = {"ID": "a3f6"}
    device = Device(raw)

    assert device.id == "A3F6"


def test_GivenARawDeviceWithInvalidIdMustRaiseException():
    raw = {"ID": "a"}

    with raises(ValueError, match=r"Invalid ID"):
        Device(raw)


def test_GivenARawDeviceWithoutIdMustRaiseException():
    raw = {"Interval": 300}

    with raises(ValueError, match=r"Invalid ID"):
        Device(raw)


def test_GivenARawDeviceMustParseIntervalLowerThan60():
    raw = {"ID": "A3F6", "Interval": 3}
    device = Device(raw)

    assert device.interval == 60


def test_GivenARawDeviceDictWithoutSubscriptionMustReturnDefault():
    raw = {"ID": "a3f6", "Interval": 300}
    device = Device(raw)

    assert ['I'] == device.subscriptionValues


def test_GivenARawDeviceDictMustReturnOrderedSubscriptionList():
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


def test_GivenARawDeviceWithAnInvalidValueMustRaiseException():
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


def test_GivenARawDeviceWithoutSubscriptionDeviceMustRaiseException():
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
