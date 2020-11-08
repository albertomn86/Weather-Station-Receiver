from src.Config import Config
from src.Socket import Socket
from src.Logger import Logger
from src.PacketManager import PacketManager
from src.FrameDecoder import FrameDecoder
import requests


def UploadData(config, payload):
    url = config.GetUploadAddress()
    if url:
        headers = {
            'content-type': 'application/json',
            'Accept-Charset': 'UTF-8'
            }
        try:
            requests.post(url, data=payload, headers=headers)
        except Exception as exception:
            raise exception


def Run(config, source, logger, uploader):
    rawFrame = source.ReadFrame()
    try:
        frame = FrameDecoder(rawFrame)
        packet = frame.GetPacket()
        logger.Write(
            logger.INFO, f"Received frame from {packet.deviceId}: {frame}")
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

    while True:
        Run(config, socket, logger, UploadData)


if __name__ == "__main__":
    main()
