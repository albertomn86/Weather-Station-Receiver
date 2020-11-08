from src.Config import Config
from src.Socket import Socket
from src.Logger import Logger
from src.PacketManager import PacketManager
from src.FrameDecoder import FrameDecoder
import requests


def UploadData(config, payload):
    url = 'http://localhost:8080/api/v1/B3ueZqE4r9sTh6T9YceJ/telemetry'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    try:
        requests.post(url, data=payload, headers=headers)
    except Exception as e:
        print(e)


def Run(config, source, logger):
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
        logger.Write(logger.WARN, error.args[0])
        return

    source.SendFrame(response)
    logger.Write(
        logger.INFO, f"Response frame sent to {packet.deviceId}: {response}")
    UploadData(config, jsonPacket)


def main():
    logger = Logger(True)
    try:
        config = Config('Config.yml')
    except Exception as exception:
        logger.Write(logger.ERR, exception.args[0])
        exit(1)

    serialPort = config.GetReceiverSerialPort()
    socket = Socket(serialPort)

    while True:
        Run(config, socket, logger)


if __name__ == "__main__":
    main()
