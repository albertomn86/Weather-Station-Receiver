from Packet import Packet
from Payload import Payload

sampleDescriptionValues = ['T', 'H', 'P', 'S', 'I', 'U', 'L', 'B']

class PayloadDecoder(object):

    def DecodeFromPacket(packet):
        sampleList = packet.Payload.split(';')
        payload = Payload()

        for sample in sampleList:
            if not sample[0] in sampleDescriptionValues:
                raise ValueError(f"Payload not valid: {sample}")

            if sample[0] == 'T':
                payload.temperature = PayloadDecoder._ParseTemperature(sample)

            elif sample[0] == 'H':
                payload.humidity = PayloadDecoder._ParseHumidity(sample)

        return payload


    def _ParseTemperature(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 20.0 or value > 50.0:
            raise ValueError(f"Invalid temperature value: {value}")

        return value

    def _ParseHumidity(sample):
        value = int(sample[1:])
        value /= 100.0

        if value < 0.0 or value > 100.0:
            raise ValueError(f"Invalid humidity value: {value}")

        return value
