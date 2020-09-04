from PayloadDecoder import PayloadDecoder
from json import dumps
from time import time


def current_milli_time():
    return int(round(time() * 1000))


class PacketManager(object):

    def __init__(self, config):
        self._config = config

    def Decode(self, packet, ts=current_milli_time()):
        if packet.From not in self._config.GetValidDevicesIdList():
            raise ValueError(f"Packet from unregistered device: {packet.From}")

        rawPayload = packet.Payload
        payload = PayloadDecoder.Decode(rawPayload)
        payloadValues = payload.GetValues()
        payloadValues['deviceId'] = packet.From

        data = {}
        data['ts'] = ts
        data['values'] = payloadValues

        json_data = dumps(data, sort_keys=True)
        return json_data
