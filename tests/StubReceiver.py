class StubReceiver(object):

    def __init__(self):
        self._frames = []

    def send_frame(self, frame):
        self._frames.append(frame)

    def read_frame(self):
        return self._frames.pop(0)
