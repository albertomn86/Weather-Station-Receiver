from time import time
from src.PacketSaver import PacketSaver
from src.PayloadEncoder import PayloadEncoder


def current_milli_time():
    return int(round(time() * 1000))


class PacketManager(object):

    def __init__(self, config):
        self._config = config

    def ProcessPacket(self, packet, ts=current_milli_time()):
        if packet.deviceId not in self._config.GetValidDevicesIdList():
            raise ValueError(
                f"Packet from unregistered device: {packet.deviceId}")

        if packet.deviceId in self._config.GetDevicesWithSubscriptionIdList():
            PacketSaver.SaveDataForSubscription(packet)

        payloadValues = packet.payload.GetValues()
        payloadValues['deviceId'] = packet.deviceId

        currentPressure = payloadValues['pressure']
        if currentPressure is not None:
            device = self._config.GetDeviceById(packet.deviceId)
            seaLevelPressure = PacketManager.getSeaLevelPressure(
                currentPressure, device.altitude)
            payloadValues['pressure'] = seaLevelPressure

        data = {}
        data['ts'] = ts
        data['values'] = payloadValues

        return data

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

        return f"K{deviceId}{encodedPayload}#"

    @staticmethod
    def getSeaLevelPressure(pressure, altitude):
        seaLevelPressure = \
            pressure / pow(1.0 - (0.000022557 * altitude), 5.256)
        return round(seaLevelPressure, 2)
