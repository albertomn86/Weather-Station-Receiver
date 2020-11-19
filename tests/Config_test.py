from pytest import raises
from Config import Config


_configFilesFolder = "tests/ConfigurationFiles/"


def test_must_assert_if_config_file_does_not_exist():

    with raises(FileNotFoundError, match=r".* fakefile.yml"):
        Config("fakefile.yml")


def test_must_assert_if_config_file_is_not_valid():

    with raises(Exception, match=r"Invalid configuration file: .*"):
        Config(_configFilesFolder + "Config_test_invalid.yml")


def test_must_assert_when_there_are_no_devices_defined():

    with raises(Exception, match=r"No devices found"):
        Config(_configFilesFolder + "Config_test_empty.yml")


def test_must_assert_when_serial_port_is_not_specified():

    with raises(Exception, match=r"Serial port not specified"):
        Config(_configFilesFolder + "Config_test_serial.yml")


def test_must_return_serial_port():

    config = Config(_configFilesFolder + "Config_test.yml")

    serialPort = config.GetReceiverSerialPort()

    assert "/dev/ttyS0" == serialPort


def test_must_return_upload_address():

    config = Config(_configFilesFolder + "Config_test.yml")

    address = config.GetUploadAddress()

    assert "http://localhost:8080/" == address


def test_must_return_upload_api_key():

    config = Config(_configFilesFolder + "Config_test.yml")

    apiKey = config.GetUploadApiKey()

    assert "ABCD1234" == apiKey


def test_loaded_config_must_contain_two_devices():

    config = Config(_configFilesFolder + "Config_test.yml")

    devices = config.GetValidDevicesIdList()

    assert len(devices) == 2
    assert "A3F6" in devices
    assert "80D4" in devices


def test_given_an_id_must_return_a_device_object():

    config = Config(_configFilesFolder + "Config_test.yml")

    device = config.GetDeviceById("A3F6")

    assert device.id == "A3F6"


def test_devices_with_subscription_must_return_one_value():

    config = Config(_configFilesFolder + "Config_test.yml")

    deviceList = config.GetDevicesWithSubscriptionIdList()

    assert ["80D4"] == deviceList
