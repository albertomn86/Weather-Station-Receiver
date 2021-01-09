from pytest import raises
from Packet import Packet
from Config import Config
from PacketManager import PacketManager
from os import path, remove
from json import dumps


config = Config("tests/ConfigurationFiles/Config_test.yml")


def test_valid_packet_from_unregistered_device_must_be_rejected():

    valid_frame = "S80D3P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(valid_frame)
    packet_manager = PacketManager(config)

    with raises(ValueError, match=r"Packet from unregistered device"):
        packet_manager.process_packet(packet)


def test_decode_must_return_dictionary_with_valid_packet():

    valid_frame = "S80D4P101812;T-304;H8000;S12;I300;L30000;B419;U067"
    packet = Packet(valid_frame)
    packet_manager = PacketManager(config)

    ts = 1598892487509
    decoded = packet_manager.process_packet(packet, ts)
    json_data = dumps(decoded, sort_keys=True)

    expected = r'{"ts": 1598892487509, "values": {"battery": 4.19, ' \
        + r'"deviceId": "80D4", "humidity": 80.0, "interval": 300, ' \
        + r'"luminosity": 300.0, "pressure": 1126.9, "status": 12, ' \
        + r'"temperature": -3.04, "uvRadiation": 0.67}}'
    assert expected == json_data


def test_if_a_device_has_subscribed_devices_the_last_payload_must_be_stored():

    valid_frame = "S80D4P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(valid_frame)
    packet_manager = PacketManager(config)

    packet_manager.process_packet(packet)

    tmp_file = "80D4.tmp"
    found = path.exists(tmp_file)

    remove(tmp_file)

    assert found


def test_if_a_device_has_not_subscribed_devices_payload_must_not_be_stored():

    valid_frame = "SA3F6P101812;T-304;H8000;S12;I300;L3000;B419;U067"
    packet = Packet(valid_frame)
    packet_manager = PacketManager(config)

    packet_manager.process_packet(packet)

    tmpFile = "A3F6.tmp"
    found = path.exists(tmpFile)

    assert not found


def test_when_generating_a_response_give_an_invalid_id_must_assert():

    packet_manager = PacketManager(config)

    with raises(ValueError, match=r"Invalid device ID: .*"):
        packet_manager.get_response_frame("A3F0")


def test_given_an_id_with_subscription_must_generate_a_response_frame():

    packet_manager = PacketManager(config)

    valid_frame = "S80D4P102012;T3087;H6000;S12;I300;L2800;B419;U077"
    packet = Packet(valid_frame)
    packet_manager.process_packet(packet)

    sample = packet_manager.get_response_frame("A3F6")

    expected_sample = "KA3F6H6000;I300;L2800;P102012;T3087;U077#"

    remove("80D4.tmp")

    assert expected_sample == sample


def test_given_an_id_with_subscription_must_generate_a_first_response_frame():

    packet_manager = PacketManager(config)

    sample = packet_manager.get_response_frame("A3F6")

    expected_sample = "KA3F6I300#"

    assert expected_sample == sample


def test_given_an_id_without_subscription_must_generate_a_response_frame():

    packet_manager = PacketManager(config)

    sample = packet_manager.get_response_frame("80D4")

    expected_sample = "K80D4I600#"

    assert expected_sample == sample
