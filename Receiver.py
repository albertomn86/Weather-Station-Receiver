from src.Config import Config
from src.Socket import Socket
from src.Logger import Logger
from src.PacketManager import PacketManager
from src.FrameDecoder import FrameDecoder
from src.DataUploader import ThingSpeak


def Run(config, source, logger, uploader):
    try:
        rawFrame = source.ReadFrame()
    except Exception as exception:
        logger.Write(logger.WARN, str(exception))

    if not rawFrame:
        return

    try:
        frame = FrameDecoder(rawFrame)
        packet = frame.GetPacket()
        logger.Write(
            logger.INFO,
            f"Received frame from {packet.deviceId}: {frame.content}")
        manager = PacketManager(config)
        jsonPacket = manager.ProcessPacket(packet)
        response = manager.GetResponseFrame(packet.deviceId)
    except ValueError as error:
        logger.Write(logger.WARN, str(error))
        return

    source.SendFrame(response)
    logger.Write(
        logger.INFO, f"Response frame sent to {packet.deviceId}: {response}")

    if uploader:
        try:
            uploader(config, jsonPacket)
        except Exception as exception:
            logger.Write(logger.ERR, str(exception))


def main():
    logger = Logger(True)
    try:
        config = Config('Config.yml')
        serialPort = config.GetReceiverSerialPort()
        socket = Socket(serialPort)
    except Exception as exception:
        logger.Write(logger.ERR, str(exception))
        exit(1)

    logger.Write(logger.INFO, "Started")
    while True:
        Run(config, socket, logger, ThingSpeak)


if __name__ == "__main__":
    main()
