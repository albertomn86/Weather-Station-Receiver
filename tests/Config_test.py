from pytest import raises
from Config import Config


_configFilesFolder = "Tests/ConfigurationFiles/"


def test_MustAssertIfConfigFileDoesNotExist():

    with raises(FileNotFoundError, match=r".* fakefile.yml"):
        Config("fakefile.yml")


def test_MustAssertIfConfigFileIsNotValid():

    with raises(Exception, match=r"Invalid configuration file: .*"):
        Config(_configFilesFolder + "Config_test_invalid.yml")


def test_MustAssertWhenThereAreNoDevicesDefined():

    with raises(Exception, match=r"No devices found"):
        Config(_configFilesFolder + "Config_test_empty.yml")


def test_LoadedConfigMustContainTwoDevices():

    config = Config(_configFilesFolder + "Config_test.yml")

    devices = config.GetValidDevicesIdList()

    assert len(devices) == 2
    assert "A3F6" in devices
    assert "80D4" in devices


def test_GivenAnIdMustReturnADeviceObject():

    config = Config(_configFilesFolder + "Config_test.yml")

    device = config.GetDeviceById("A3F6")

    assert device.id == "A3F6"


def test_DevicesWithSubscriptionMustReturnOneValue():

    config = Config(_configFilesFolder + "Config_test.yml")

    deviceList = config.GetDevicesWithSubscriptionIdList()

    assert ["80D4"] == deviceList
