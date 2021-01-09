from src.Config import Config
from src.Socket import Socket
from src.Logger import Logger
from src.PacketManager import PacketManager
from src.FrameDecoder import FrameDecoder
from src.DataUploader import thing_speak_uploader


def run(config, source, logger, uploader):
    try:
        raw_frame = source.read_frame()
    except Exception as exception:
        logger.Write(logger.WARN, str(exception))
        return

    try:
        frame = FrameDecoder(raw_frame)
        packet = frame.get_packet()
        logger.write(
            logger.INFO,
            f"Received frame from {packet.device_id}: {frame.content}")
        manager = PacketManager(config)
        json_packet = manager.process_packet(packet)
        response = manager.get_response_frame(packet.device_id)
    except ValueError as error:
        logger.write(logger.WARN, str(error))
        return

    source.send_frame(response)
    logger.write(
        logger.INFO, f"Response frame sent to {packet.device_id}: {response}")

    if uploader:
        try:
            uploader(config, json_packet)
            logger.write(logger.INFO, "Data uploaded")
        except Exception as exception:
            logger.write(logger.ERR, str(exception))


def main():
    logger = Logger(True)
    try:
        config = Config('Config.yml')
        serial_port = config.get_receiver_serial_port()
        socket = Socket(serial_port)
    except Exception as exception:
        logger.write(logger.ERR, str(exception))
        exit(1)

    logger.write(logger.INFO, "Started")
    while True:
        run(config, socket, logger, thing_speak_uploader)


if __name__ == "__main__":
    main()
