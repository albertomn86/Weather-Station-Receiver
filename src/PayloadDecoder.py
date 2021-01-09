from src.Payload import Payload


class PayloadDecoder(object):

    @staticmethod
    def decode(raw):
        sample_list = raw.split(';')
        payload = Payload()

        for sample in sample_list:

            if sample[0] == 'T':
                payload.temperature = \
                    PayloadDecoder.__parse_temperature(sample)

            elif sample[0] == 'H':
                payload.humidity = PayloadDecoder.__parse_humidity(sample)

            elif sample[0] == 'P':
                payload.pressure = PayloadDecoder.__parse_pressure(sample)

            elif sample[0] == 'L':
                payload.luminosity = PayloadDecoder.__parse_luminosity(sample)

            elif sample[0] == 'S':
                payload.status = PayloadDecoder.__parse_status(sample)

            elif sample[0] == 'B':
                payload.battery = PayloadDecoder.__parse_battery(sample)

            elif sample[0] == 'I':
                payload.interval = PayloadDecoder.__parse_interval(sample)

            elif sample[0] == 'U':
                payload.uv_radiation = \
                    PayloadDecoder.__parse_uv_radiation(sample)

            else:
                raise ValueError(f"Payload not valid: {sample}")

        return payload

    @staticmethod
    def __parse_temperature(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < -20.0 or value > 50.0:
            raise ValueError(f"Invalid temperature value: {value}")

        return value

    @staticmethod
    def __parse_humidity(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.0 or value > 100.0:
            raise ValueError(f"Invalid humidity value: {value}")

        return value

    @staticmethod
    def __parse_luminosity(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.0:
            raise ValueError(f"Invalid luminosity value: {value}")

        return value

    @staticmethod
    def __parse_status(sample):
        value = int(sample[1:])

        if value < 0 or value > 31:
            raise ValueError(f"Invalid status value: {value}")

        return value

    @staticmethod
    def __parse_battery(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.00:
            raise ValueError(f"Invalid battery voltage value: {value}")

        return value

    @staticmethod
    def __parse_interval(sample):
        value = int(sample[1:])

        if value <= 0:
            raise ValueError(f"Invalid interval value: {value}")

        return value

    @staticmethod
    def __parse_uv_radiation(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.00:
            raise ValueError(f"Invalid UV radiation value: {value}")

        return value

    @staticmethod
    def __parse_pressure(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 800.00 or value > 1100:
            raise ValueError(f"Invalid pressure value: {value}")

        return value
