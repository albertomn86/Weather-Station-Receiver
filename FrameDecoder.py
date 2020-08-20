
class FrameDecoder(object):

    def __init__(self, frame):

        if self.IsValid(frame):
            self._frame = frame
        else:
            raise ValueError("Invalid frame {0}".format(frame))


    @staticmethod
    def IsValid(testFrame):

        if not testFrame.endswith('#'):
            return False

        if not (testFrame.startswith('S') or testFrame.startswith('K')):
            return False

        return True
