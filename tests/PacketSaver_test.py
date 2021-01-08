from Packet import Packet
from PacketSaver import PacketSaver
from os import remove


def test_given_an_id_return_stored_payload():

    validFrame = "SA3F6P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(validFrame)

    PacketSaver.SaveDataForSubscription(packet)

    readPayload = PacketSaver.GetSavedPayloadFromFile("A3F6")

    remove("A3F6.tmp")

    assert 4.19 == readPayload.battery


def test_when_the_file_does_not_exist_must_return_empty_payload():

    readPayload = PacketSaver.GetSavedPayloadFromFile("A3F6")

    assert readPayload.battery is None
