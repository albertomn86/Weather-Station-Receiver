from sys import path as sysPath
from os import path as osPath
sysPath.append(osPath.abspath("./"))
from FrameDecoder import FrameDecoder
import pytest

def test_ValidFrameMustHaveMoreThanSixCharacters():

    frame = "SA3D0#"

    with pytest.raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_ValidFrameMustEndWithEndCharacter():

    frame = "SA3F64FD0#"

    FrameDecoder(frame)


def test_FramesWithInvalidTerminationMustReturnException():

    frame = "SA3F64FD0Q"

    with pytest.raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_ValidFrameMustStartWithDefinedHeader():

    frame = "K80D44FD0#"

    FrameDecoder(frame)


def test_FramesWithInvalidFirstCharacterMustReturnException():

    frame = "XA3F64FD0#"

    with pytest.raises(ValueError, match=r"Invalid frame: .*"):
        FrameDecoder(frame)


def test_ValidFrameMustReturnAValidPacket():

    frame = "S80D44FD0#"

    packet = FrameDecoder(frame).GetPacket()

    assert packet.Type == "S"
    assert packet.From == "80D4"
    assert packet.Payload == "4FD0"
