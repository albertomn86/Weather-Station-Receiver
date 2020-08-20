import sys
import os
import pytest
sys.path.append(os.path.abspath("../"))
from FrameDecoder import FrameDecoder


def test_ValidFrameMustEndWithEndCharacter():

    frame = "SA3F6@4FD0#"

    FrameDecoder(frame)


def test_FramesWithInvalidTerminationMustReturnException():

    frame = "SA3F6@4FD0Q"

    with pytest.raises(ValueError, match=r"Invalid frame .*"):
        FrameDecoder(frame)


def test_ValidFrameMustStartWithDefinedHeader():

    frame = "K80D4@4FD0#"

    FrameDecoder(frame)


def test_FramesWithInvalidFirstCharacterMustReturnException():

    frame = "XA3F6@4FD0#"

    with pytest.raises(ValueError, match=r"Invalid frame .*"):
        FrameDecoder(frame)
