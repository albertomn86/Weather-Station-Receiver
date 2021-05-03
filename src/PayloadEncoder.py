from src.Payload import Payload
from typing import Any


class PayloadEncoder(object):

    @staticmethod
    def encode(payload: Payload) -> str:
        generated = ""

        if payload.battery is not None:
            generated += f"B{encode_decimal(payload.battery)};"

        if payload.humidity is not None:
            generated += f"H{encode_decimal(payload.humidity)};"

        if payload.interval is not None:
            generated += f"I{payload.interval};"

        if payload.luminosity is not None:
            generated += f"L{encode_decimal(payload.luminosity)};"

        if payload.pressure is not None:
            generated += f"P{encode_decimal(payload.pressure)};"

        if payload.status is not None:
            generated += f"S{payload.status};"

        if payload.temperature is not None:
            generated += f"T{encode_decimal(payload.temperature)};"

        if payload.uv_radiation is not None:
            generated += f"U{encode_decimal(payload.uv_radiation)};"

        return generated[:-1]


def encode_decimal(value: Any) -> str:
    encoded = "{0:.2f}".format(value)
    encoded = encoded.replace(".", "")
    return encoded
