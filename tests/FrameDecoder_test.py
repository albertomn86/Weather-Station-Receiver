from pytest import raises
from FrameDecoder import FrameDecoder


def test_valid_frame_must_have_more_than_six_characters():

    frame = "SA3D0#"

    with raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_valid_frame_must_end_with_end_character():

    frame = "SA3F64FD0#"

    FrameDecoder(frame)


def test_frames_with_invalid_termination_must_return_exception():

    frame = "SA3F64FD0Q"

    with raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_valid_frame_must_start_with_defined_header():

    frame = "K80D44FD0#"

    FrameDecoder(frame)


def test_frames_with_invalid_first_character_must_return_exception():

    frame = "XA3F64FD0#"

    with raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_valid_frame_must_return_a_valid_packet():

    frame = "S80D4P101812;T-304;H8000#"

    decodedFrame = FrameDecoder(frame)
    packet = decodedFrame.GetPacket()

    assert packet.type == "S"
    assert packet.deviceId == "80D4"
    assert packet.payload.temperature == -3.04
    assert packet.payload.humidity == 80.0
    assert packet.payload.pressure == 1018.12
