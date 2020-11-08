from src.Config import Config
from src.Socket import Socket
from src.Logger import Logger
from src.PacketManager import PacketManager
from src.FrameDecoder import FrameDecoder


def UploadData(data):
    pass


def Run(config, source, logger):
    rawFrame = source.ReadFrame()
    try:
        frame = FrameDecoder(rawFrame)
        packet = frame.GetPacket()
        manager = PacketManager(config)
        jsonPacket = manager.ProcessPacket(packet)
        response = manager.GetResponseFrame(packet.deviceId)
    except ValueError as error:
        logger.Write(error.args[0])
        return

    source.SendFrame(response)
    UploadData(jsonPacket)


def main():
    config = Config('Config.yml')
    logger = Logger()
    socket = Socket('/dev/ttyS0')

    while True:
        Run(config, socket, logger)


if __name__ == "__main__":
    main()
