from pytest import raises
from FrameDecoder import FrameDecoder


def test_ValidFrameMustHaveMoreThanSixCharacters():

    frame = "SA3D0#"

    with raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_ValidFrameMustEndWithEndCharacter():

    frame = "SA3F64FD0#"

    FrameDecoder(frame)


def test_FramesWithInvalidTerminationMustReturnException():

    frame = "SA3F64FD0Q"

    with raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_ValidFrameMustStartWithDefinedHeader():

    frame = "K80D44FD0#"

    FrameDecoder(frame)


def test_FramesWithInvalidFirstCharacterMustReturnException():

    frame = "XA3F64FD0#"

    with raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_ValidFrameMustReturnAValidPacket():

    frame = "S80D4P101812;T-304;H8000#"

    decodedFrame = FrameDecoder(frame)
    packet = decodedFrame.GetPacket()

    assert packet.type == "S"
    assert packet.deviceId == "80D4"
    assert packet.payload.temperature == -3.04
    assert packet.payload.humidity == 80.0
    assert packet.payload.pressure == 1018.12
