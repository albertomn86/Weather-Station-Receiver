from src.Config import Config
from src.Socket import Socket
from src.Logger import Logger
from src.FrameDecoder import FrameDecoder


def Receiver(config, source, logger):
    rawFrame = source.ReadFrame()
    try:
        FrameDecoder(rawFrame)
    except ValueError as error:
        logger.Write(error.args[0])


def main():
    config = Config('Config.yml')
    logger = Logger()
    socket = Socket('/dev/ttyS0')

    while True:
        Receiver(config, socket, logger)


if __name__ == "__main__":
    main()
