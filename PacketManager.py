from json import dumps
from time import time
from PacketSaver import PacketSaver
from PayloadEncoder import PayloadEncoder


def current_milli_time():
    return int(round(time() * 1000))


class PacketManager(object):

    def __init__(self, config):
        self._config = config

    def ProcessPacket(self, packet, ts=current_milli_time()):
        if packet.deviceId not in self._config.GetValidDevicesIdList():
            raise ValueError(f"Packet from unregistered device: \
                {packet.deviceId}")

        if packet.deviceId in self._config.GetDevicesWithSubscriptionIdList():
            PacketSaver.SaveDataForSubscription(packet)

        payloadValues = packet.payload.GetValues()
        payloadValues['deviceId'] = packet.deviceId

        data = {}
        data['ts'] = ts
        data['values'] = payloadValues

        json_data = dumps(data, sort_keys=True)
        return json_data

    def GetResponseFrame(self, deviceId):
        if deviceId not in self._config.GetValidDevicesIdList():
            raise ValueError(f"Invalid device ID: {deviceId}")

        deviceConfig = self._config.GetDeviceById(deviceId)
        subscribedDevice = deviceConfig.subscriptionDevice
        subscribedDeviceValues = deviceConfig.subscriptionValues

        newPayload = PacketSaver.GetSavedPayloadFromFile(subscribedDevice)
        newPayload.KeepValues(subscribedDeviceValues)
        newPayload.interval = deviceConfig.interval

        encodedPayload = PayloadEncoder.Encode(newPayload)

        return f"K{deviceId}{encodedPayload}"
