from Packet import Packet
from PacketSaver import PacketSaver
from os import remove


def test_given_an_id_return_stored_payload():

    valid_frame = "SA3F6P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(valid_frame)

    PacketSaver.save_data_for_subscription(packet)

    read_payload = PacketSaver.get_saved_payload_from_file("A3F6")

    remove("A3F6.tmp")

    assert 4.19 == read_payload.battery


def test_when_the_file_does_not_exist_must_return_empty_payload():

    read_payload = PacketSaver.get_saved_payload_from_file("A3F6")

    assert read_payload.battery is None
