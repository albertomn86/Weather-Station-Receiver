class PayloadEncoder():

    def Encode(payload):
        generated = ""

        if payload.battery is not None:
            generated += f"B{EncodeDecimal(payload.battery)};"

        if payload.humidity is not None:
            generated += f"H{EncodeDecimal(payload.humidity)};"

        if payload.interval is not None:
            generated += f"I{payload.interval};"

        if payload.luminosity is not None:
            generated += f"L{EncodeDecimal(payload.luminosity)};"

        if payload.pressure is not None:
            generated += f"P{EncodeDecimal(payload.pressure)};"

        if payload.status is not None:
            generated += f"S{payload.status};"

        if payload.temperature is not None:
            generated += f"T{EncodeDecimal(payload.temperature)};"

        if payload.uvRadiation is not None:
            generated += f"U{EncodeDecimal(payload.uvRadiation)};"

        return generated[:-1]


def EncodeDecimal(value):
    encoded = "{0:.2f}".format(value)
    encoded = encoded.replace(".", "")
    return encoded
