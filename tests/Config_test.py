from pytest import raises
from Config import Config, ConfigException


config_files_folder = "tests/ConfigurationFiles/"


def test_must_assert_if_config_file_does_not_exist():

    with raises(FileNotFoundError, match=r".* fakefile.yml"):
        Config("fakefile.yml")


def test_must_assert_if_config_file_is_not_valid():

    with raises(ConfigException, match=r"Invalid configuration file: .*"):
        Config(config_files_folder + "Config_test_invalid.yml")


def test_must_assert_when_there_are_no_devices_defined():

    with raises(ConfigException, match=r"No devices found"):
        Config(config_files_folder + "Config_test_empty.yml")


def test_must_assert_when_serial_port_is_not_specified():

    with raises(ConfigException, match=r"Serial port not specified"):
        Config(config_files_folder + "Config_test_serial.yml")


def test_must_return_serial_port():

    config = Config(config_files_folder + "Config_test.yml")

    serial_port = config.get_receiver_serial_port()

    assert "/dev/ttyS0" == serial_port


def test_must_return_upload_address():

    config = Config(config_files_folder + "Config_test.yml")

    address = config.get_upload_address()

    assert "http://localhost:8080/" == address


def test_must_return_upload_api_key():

    config = Config(config_files_folder + "Config_test.yml")

    api_key = config.get_upload_api_key()

    assert "ABCD1234" == api_key


def test_loaded_config_must_ignore_repeated_devices():

    config = Config(config_files_folder + "Config_test.yml")

    devices = config.get_valid_devices_id_list()

    assert len(devices) == 2
    assert "A3F6" in devices
    assert "80D4" in devices


def test_given_an_id_must_return_a_device_object():

    config = Config(config_files_folder + "Config_test.yml")

    device = config.get_device_by_id("A3F6")

    assert device.id == "A3F6"


def test_devices_with_subscription_must_return_one_value():

    config = Config(config_files_folder + "Config_test.yml")

    devices_list = config.get_devices_with_subscription()

    assert ["80D4"] == devices_list
