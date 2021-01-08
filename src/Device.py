class Device(object):

    def __init__(self, raw):
        self.id = Device._ValidateId(raw.get("ID"))
        self.interval = Device._ValidateInterval(raw.get("Interval"))
        self.subscriptionDevice, self.subscriptionValues = \
            Device._ValidateSubscription(raw.get("Subscription"))
        self.altitude = Device._ValidateAltitude(raw.get("Altitude"))

    @staticmethod
    def _ValidateId(rawId):
        if rawId is None or len(rawId) != 4:
            raise ValueError("Invalid ID")

        return rawId.upper()

    @staticmethod
    def _ValidateInterval(interval):
        if interval is None or interval < 60:
            return 60
        else:
            return interval

    @staticmethod
    def _ValidateAltitude(altitude):
        if altitude is None or altitude < 0:
            altitude = 0
        return altitude

    @staticmethod
    def _ValidateSubscription(rawSubscription):
        subscription = ['I']
        device = None
        if rawSubscription is not None:
            values = rawSubscription.get("Values").split(',')
            for item in values:
                item = item.upper().strip()
                if item in ['T', 'H', 'P', 'U', 'L', 'S', 'B']:
                    subscription.append(item)
                else:
                    raise ValueError(f"Invalid subscription value: '{item}'")
            subscription.sort()

            device = rawSubscription.get("Device")
            if device is None:
                raise ValueError("Subscription device not found")

        return device, subscription
