from yaml import safe_load, YAMLError
from os import path
from Device import Device


class Config(object):

    def __init__(self, file):

        if not path.exists(file):
            raise FileNotFoundError(f"Config file not found: {file}")

        with open(file, 'r') as stream:
            try:
                self._config = safe_load(stream)
            except YAMLError:
                raise Exception(f"Invalid configuration file: {file}")

        if self._config is None:
            raise Exception(f"Empty configuration file: {file}")

        self._devicesList, self._allowedDevicesIdList, \
            self._devicesWithSubsciption = \
            Config._ParseDevices(self._config)

    def _ParseDevices(config):
        devices = config.get("Devices")
        if devices is None:
            raise Exception("No devices found")

        deviceList = []
        allowedIdList = []
        devicesWithSubscription = []
        for item in devices:
            device = Device(item)
            deviceList.append(device)
            allowedIdList.append(device.id)
            if device.subscriptionDevice is not None:
                devicesWithSubscription.append(device.subscriptionDevice)

        return deviceList, allowedIdList, devicesWithSubscription

    def GetValidDevicesIdList(self):
        return self._allowedDevicesIdList

    def GetDeviceById(self, id):
        return [x for x in self._devicesList if x.id == id][0]

    def GetDevicesWithSubscriptionIdList(self):
        return self._devicesWithSubsciption
