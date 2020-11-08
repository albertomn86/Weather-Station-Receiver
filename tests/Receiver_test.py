from Receiver import Run
from Config import Config
from Logger import Logger
from tests.StubReceiver import StubReceiver
from os import remove

config = Config("tests/ConfigurationFiles/Config_test.yml")


def test_ReceiverMustShowErrorIfFrameIsInvalid():

    logger = Logger()
    stub = StubReceiver()
    testFrame = "W80D44FD0#"
    stub.SendFrame(testFrame)
    expectedMsg = f"Invalid frame: {testFrame}"

    Run(config, stub, logger)

    assert expectedMsg == logger.lastMessage


def test_ReceiverMustShowErrorIfPayloadIsInvalid():

    logger = Logger()
    stub = StubReceiver()
    testFrame = "S80D44FD0#"
    stub.SendFrame(testFrame)
    expectedMsg = "Payload not valid: 4FD0"

    Run(config, stub, logger)

    assert expectedMsg == logger.lastMessage


def test_ReceiverMustShowErrorIfPacketComesFromUnregisteredDevice():

    logger = Logger()
    stub = StubReceiver()
    testFrame = "S80D3P101812;T-304;H8000;S12;I300;L3000;B419;U067#"
    stub.SendFrame(testFrame)
    expectedMsg = "Packet from unregistered device: 80D3"

    Run(config, stub, logger)

    assert expectedMsg == logger.lastMessage


def test_ReceiverMustSendFrameWhenAValidMessageIsReceived():

    logger = Logger()
    stub = StubReceiver()
    stub.SendFrame("S80D4P101812;T-304;H8000;S12;I300;L3000;B419;U067#")
    stub.SendFrame("SA3F6I300#")

    Run(config, stub, logger)
    Run(config, stub, logger)

    expectedFrame1 = "K80D4I600#"
    expectedFrame2 = "KA3F6H8000;I300;L3000;P101812;T-304;U067#"

    remove("80D4.tmp")

    assert expectedFrame1 == stub.ReadFrame()
    assert expectedFrame2 == stub.ReadFrame()
