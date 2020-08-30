from yaml import safe_load, YAMLError
from os import path


class Config(object):

    def __init__(self, file):

        if not path.exists(file):
            raise FileNotFoundError(f"Config file not found: {file}")

        with open(file, 'r') as stream:
            try:
                self._config = safe_load(stream)
            except YAMLError:
                raise Exception("Invalif config file")

    def GetDevices(self):

        return self._config.get("devices")
