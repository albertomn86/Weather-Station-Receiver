from pytest import raises
from Config import Config


def test_MustAssertIfConfigFileDoesNotExist():

    with raises(FileNotFoundError, match=r".* fakefile.yml"):
        Config("fakefile.yml")


def test_MustAssertIfConfigFileIsNotValid():

    with raises(Exception, match=r"Invalid configuration file: .*"):
        Config("Tests/Config_test_invalid.yml")


def test_LoadedConfigMustContainTwoDevices():

    config = Config("Tests/Config_test.yml")

    devices = config.GetDevices()

    assert len(devices) == 2
    assert "A3F6" in devices
    assert "80D4" in devices
