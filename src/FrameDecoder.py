from src.Packet import Packet


class FrameDecoder(object):

    def __init__(self, frame: str):
        if FrameDecoder.__is_valid(frame):
            self.content = frame
        else:
            raise ValueError(f"Invalid frame: {frame}")

    @staticmethod
    def __is_valid(test_frame: str) -> bool:
        if len(test_frame) <= 6:
            return False

        if not test_frame.endswith('#'):
            return False

        if not (test_frame.startswith('S') or test_frame.startswith('K')):
            return False

        return True

    def get_packet(self) -> Packet:
        packet = Packet(self.content[:-1])

        return packet
