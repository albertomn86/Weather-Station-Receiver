from yaml import safe_load, YAMLError
from os import path
from src.Device import Device


class Config(object):

    def __init__(self, file):

        if not path.exists(file):
            raise FileNotFoundError(f"Config file not found: {file}")

        with open(file, 'r') as stream:
            try:
                self.__config = safe_load(stream)
            except YAMLError:
                raise Exception(f"Invalid configuration file: {file}")

        if self.__config is None:
            raise Exception(f"Empty configuration file: {file}")

        self.__serial_port = Config.__parse_receiver(self.__config)

        self.__upload_addres, \
            self.__upload_api_key = Config.__parse_upload(self.__config)

        self.__devices_list, \
            self.__allowed_devices_id_list, \
            self.__devices_with_subsciption = \
            Config.__parse_devices(self.__config)

    @staticmethod
    def __parse_receiver(config):
        receiver = config.get("Receiver")
        if receiver is not None:
            serial_port = receiver.get("SerialPort")
            if serial_port is not None:
                return serial_port
        raise Exception("Serial port not specified")

    @staticmethod
    def __parse_upload(config):
        address = None
        api_key = None
        upload = config.get("Upload")
        if upload is not None:
            address = upload.get("Address")
            api_key = upload.get("ApiKey")
        return address, api_key

    @staticmethod
    def __parse_devices(config):
        devices = config.get("Devices")
        if devices is None:
            raise Exception("No devices found")

        device_list = []
        allowed_id_list = []
        devices_with_subscription = []
        for item in devices:
            device = Device(item)
            device_list.append(device)
            allowed_id_list.append(device.id)
            if device.subscription_device is not None:
                devices_with_subscription.append(device.subscription_device)

        return device_list, allowed_id_list, devices_with_subscription

    def get_valid_devices_id_list(self):
        return self.__allowed_devices_id_list

    def get_device_by_id(self, id):
        return [x for x in self.__devices_list if x.id == id][0]

    def get_devices_with_subscription(self):
        return self.__devices_with_subsciption

    def get_receiver_serial_port(self):
        return self.__serial_port

    def get_upload_address(self):
        return self.__upload_addres

    def get_upload_api_key(self):
        return self.__upload_api_key
