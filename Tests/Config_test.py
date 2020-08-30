from sys import path as sysPath
from os import path as osPath
sysPath.append(osPath.abspath("./"))
from Config import Config
import pytest


def test_MustAssertIfConfigFileDoesntExist():

    with pytest.raises(FileNotFoundError, match=r".* fakefile.yml"):
        Config("fakefile.yml")


def test_LoadedConfigMustContainTwoDevices():

    config = Config("Tests/Config_test.yml")

    devices = config.GetDevices()

    assert len(devices) == 2
    assert "A3F6" in devices
    assert "80D4" in devices
