from time import time
from src.Packet import Packet
from src.PacketSaver import PacketSaver
from src.PayloadEncoder import PayloadEncoder


def current_milli_time():
    return int(round(time() * 1000))


class PacketManager(object):

    def __init__(self, config):
        self.__config = config

    def process_packet(self, packet: Packet, ts=current_milli_time()) -> dict:
        if packet.device_id not in self.__config.get_valid_devices_id_list():
            raise ValueError(
                f"Packet from unregistered device: {packet.device_id}")

        if packet.device_id in self.__config.get_devices_with_subscription():
            PacketSaver.save_data_for_subscription(packet)

        payload_values = packet.payload.get_values()
        payload_values['deviceId'] = packet.device_id

        current_pressure = payload_values['pressure']
        if current_pressure is not None:
            device = self.__config.get_device_by_id(packet.device_id)
            payload_values['pressure'] = PacketManager.get_sea_level_pressure(
                current_pressure, device.altitude)

        data = {}
        data['ts'] = ts
        data['values'] = payload_values

        return data

    def get_response_frame(self, device_id: str) -> str:
        if device_id not in self.__config.get_valid_devices_id_list():
            raise ValueError(f"Invalid device ID: {device_id}")

        device_config = self.__config.get_device_by_id(device_id)
        subscribed_device = device_config.subscription_device
        subscribed_device_values = device_config.subscription_values

        new_payload = \
            PacketSaver.get_saved_payload_from_file(subscribed_device)
        new_payload.keep_values(subscribed_device_values)
        new_payload.interval = device_config.interval

        encoded_payload = PayloadEncoder.encode(new_payload)

        return f"K{device_id}{encoded_payload}#"

    @staticmethod
    def get_sea_level_pressure(pressure: float, altitude: int) -> float:
        sea_level_pressure = \
            pressure / pow(1.0 - (0.000022557 * altitude), 5.256)
        return round(sea_level_pressure, 2)
