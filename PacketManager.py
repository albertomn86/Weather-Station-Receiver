from json import dumps
from time import time
import pickle


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
            PacketManager._SaveDataForSubscription(packet)

        payloadValues = packet.payload.GetValues()
        payloadValues['deviceId'] = packet.deviceId

        data = {}
        data['ts'] = ts
        data['values'] = payloadValues

        json_data = dumps(data, sort_keys=True)
        return json_data

    def _SaveDataForSubscription(packet):
        with open(f"{packet.deviceId}.tmp", "wb") as tmpFile:
            pickle.dump(packet.payload, tmpFile, pickle.HIGHEST_PROTOCOL)

    def _GetSavedPayloadFromFile(deviceId):
        with open(f"{deviceId}.tmp", "rb") as tmpFile:
            payload = pickle.load(tmpFile)
            return payload
