from Config import Config
from PayloadDecoder import PayloadDecoder
from json import dumps
from time import time


def current_milli_time():
    return int(round(time() * 1000))


class PacketManager(object):

    def __init__(self, config=Config("Config.yml")):
        self._config = config

    def Decode(self, packet, ts=current_milli_time()):
        if packet.From not in self._config.GetDevices():
            raise ValueError(f"Packet from unregistered device: {packet.From}")

        payload = PayloadDecoder.DecodeFromPacket(packet)
        payloadData = payload.GetValues()
        payloadData['deviceId'] = packet.From

        data = {}
        data['ts'] = ts
        data['values'] = payloadData

        json_data = dumps(data, sort_keys=True)
        return json_data
