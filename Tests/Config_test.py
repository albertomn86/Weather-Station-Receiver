import sys
import os
import pytest
sys.path.append(os.path.abspath("./"))
from Config import Config


def test_MustAssertIfConfigFileDoesntExist():

    with pytest.raises(FileNotFoundError, match=r".* fakefile.yml"):
        config = Config("fakefile.yml")


def test_LoadedConfigMustContainTwoDevices():

    config = Config("Tests/Config_test.yml")

    devices = config.GetDevices()

    assert len(devices) == 2
