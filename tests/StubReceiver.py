class StubReceiver(object):

    def __init__(self):
        self._frames = []

    def SendFrame(self, frame):
        self._frames.append(frame)

    def ReadFrame(self):
        return self._frames.pop(0)
