from Receiver import run
from Config import Config
from Logger import Logger
from tests.StubReceiver import StubReceiver
from os import remove

config = Config("tests/ConfigurationFiles/Config_test.yml")


def test_receiver_must_show_error_if_frame_is_invalid():

    logger = Logger()
    stub = StubReceiver()
    test_frame = "W80D44FD0#"
    stub.send_frame(test_frame)
    expected_msg = f"Invalid frame: {test_frame}"

    run(config, stub, logger, None)

    assert expected_msg == logger.last_message


def test_receiver_must_show_error_if_payload_is_invalid():

    logger = Logger()
    stub = StubReceiver()
    test_frame = "S80D44FD0#"
    stub.send_frame(test_frame)
    expected_msg = "Payload not valid: 4FD0"

    run(config, stub, logger, None)

    assert expected_msg == logger.last_message


def test_receiver_must_show_error_if_packet_comes_from_unregistered_device():

    logger = Logger()
    stub = StubReceiver()
    test_frame = "S80D3P101812;T-304;H8000;S12;I300;L3000;B419;U067#"
    stub.send_frame(test_frame)
    expected_msg = "Packet from unregistered device: 80D3"

    run(config, stub, logger, None)

    assert expected_msg == logger.last_message


def test_receiver_must_send_frame_when_a_valid_message_is_received():

    logger = Logger()
    stub = StubReceiver()
    stub.send_frame("S80D4P101812;T-304;H8000;S12;I300;L3000;B419;U067#")
    stub.send_frame("SA3F6I300#")

    run(config, stub, logger, None)
    run(config, stub, logger, None)

    expected_frame_1 = "K80D4I600#"
    expected_frame_2 = "KA3F6H8000;I300;L3000;P101812;T-304;U067#"

    remove("80D4.tmp")

    assert expected_frame_1 == stub.read_frame()
    assert expected_frame_2 == stub.read_frame()
