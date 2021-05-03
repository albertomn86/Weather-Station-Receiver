class StubReceiver(object):

    def __init__(self):
        self._frames = []

    def send_frame(self, frame: str):
        self._frames.append(frame)

    def read_frame(self) -> str:
        return self._frames.pop(0)
