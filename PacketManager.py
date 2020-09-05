from json import dumps
from time import time


def current_milli_time():
    return int(round(time() * 1000))


class PacketManager(object):

    def __init__(self, config):
        self._config = config

    def DecodePacket(self, packet, ts=current_milli_time()):
        if packet.deviceId not in self._config.GetValidDevicesIdList():
            raise ValueError(f"Packet from unregistered device: \
                {packet.deviceId}")

        payloadValues = packet.payload.GetValues()
        payloadValues['deviceId'] = packet.deviceId

        data = {}
        data['ts'] = ts
        data['values'] = payloadValues

        json_data = dumps(data, sort_keys=True)
        return json_data
