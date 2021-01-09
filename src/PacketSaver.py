import pickle
from os import path
from src.Payload import Payload


class PacketSaver():

    @staticmethod
    def save_data_for_subscription(packet):
        with open(f"{packet.device_id}.tmp", "wb") as tmp_file:
            pickle.dump(packet.payload, tmp_file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def get_saved_payload_from_file(device_id):
        tmp_filename = f"{device_id}.tmp"
        if path.exists(tmp_filename):
            with open(tmp_filename, "rb") as tmp_file:
                payload = pickle.load(tmp_file)
                return payload
        else:
            return Payload()
