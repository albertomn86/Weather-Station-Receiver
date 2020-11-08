from Receiver import Receiver
from Config import Config
from Logger import Logger
from tests.StubReceiver import StubReceiver

config = Config("tests/ConfigurationFiles/Config_test.yml")


def test_MustShowErrorIfFrameIsInvalid():

    logger = Logger()
    stub = StubReceiver()
    testFrame = "W80D44FD0#"
    stub.LoadFrame(testFrame)
    expectedMsg = f"Invalid frame: {testFrame}"

    Receiver(config, stub, logger)

    assert expectedMsg == logger.lastMessage
