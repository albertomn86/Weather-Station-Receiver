from typing import Any, Optional


class Device(object):

    def __init__(self, raw: dict):
        self.id = Device.__validate_id(raw.get("ID"))
        self.interval = Device.__validate_interval(raw.get("Interval"))
        self.subscription_device, self.subscription_values = \
            Device.__validate_subscription(raw.get("Subscription"))
        self.altitude = Device.__validate_altitude(raw.get("Altitude"))

    @staticmethod
    def __validate_id(raw_id: Optional[Any]) -> str:
        if raw_id is None or len(raw_id) != 4:
            raise ValueError("Invalid ID")

        return raw_id.upper()

    @staticmethod
    def __validate_interval(interval: Optional[Any]) -> int:
        if interval is None or interval < 60:
            return 60
        else:
            return interval

    @staticmethod
    def __validate_altitude(altitude: Optional[Any]) -> int:
        if altitude is None or altitude < 0:
            altitude = 0
        return altitude

    @staticmethod
    def __validate_subscription(raw_subscription: dict) -> tuple[Any, Any]:
        subscription = ['I']
        device = None
        if raw_subscription is not None:
            values = raw_subscription.get("Values")
            if values is not None:
                for item in values.split(','):
                    item = item.upper().strip()
                    if item in ['T', 'H', 'P', 'U', 'L', 'S', 'B']:
                        subscription.append(item)
                    else:
                        raise ValueError(
                            f"Invalid subscription value: '{item}'")
                subscription.sort()

                device = raw_subscription.get("Device")
                if device is None:
                    raise ValueError("Subscription device not found")

        return device, subscription
