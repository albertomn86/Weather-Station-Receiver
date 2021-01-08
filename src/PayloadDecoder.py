from src.Payload import Payload


class PayloadDecoder():

    def Decode(raw):
        sampleList = raw.split(';')
        payload = Payload()

        for sample in sampleList:

            if sample[0] == 'T':
                payload.temperature = PayloadDecoder._ParseTemperature(sample)

            elif sample[0] == 'H':
                payload.humidity = PayloadDecoder._ParseHumidity(sample)

            elif sample[0] == 'P':
                payload.pressure = PayloadDecoder._ParsePressure(sample)

            elif sample[0] == 'L':
                payload.luminosity = PayloadDecoder._ParseLuminosity(sample)

            elif sample[0] == 'S':
                payload.status = PayloadDecoder._ParseStatus(sample)

            elif sample[0] == 'B':
                payload.battery = PayloadDecoder._ParseBattery(sample)

            elif sample[0] == 'I':
                payload.interval = PayloadDecoder._ParseInterval(sample)

            elif sample[0] == 'U':
                payload.uvRadiation = PayloadDecoder._ParseUVRadiation(sample)

            else:
                raise ValueError(f"Payload not valid: {sample}")

        return payload

    @staticmethod
    def _ParseTemperature(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < -20.0 or value > 50.0:
            raise ValueError(f"Invalid temperature value: {value}")

        return value

    @staticmethod
    def _ParseHumidity(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.0 or value > 100.0:
            raise ValueError(f"Invalid humidity value: {value}")

        return value

    @staticmethod
    def _ParseLuminosity(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.0:
            raise ValueError(f"Invalid luminosity value: {value}")

        return value

    @staticmethod
    def _ParseStatus(sample):
        value = int(sample[1:])

        if value < 0 or value > 31:
            raise ValueError(f"Invalid status value: {value}")

        return value

    @staticmethod
    def _ParseBattery(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.00:
            raise ValueError(f"Invalid battery voltage value: {value}")

        return value

    @staticmethod
    def _ParseInterval(sample):
        value = int(sample[1:])

        if value <= 0:
            raise ValueError(f"Invalid interval value: {value}")

        return value

    @staticmethod
    def _ParseUVRadiation(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.00:
            raise ValueError(f"Invalid UV radiation value: {value}")

        return value

    @staticmethod
    def _ParsePressure(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 800.00 or value > 1100:
            raise ValueError(f"Invalid pressure value: {value}")

        return value
