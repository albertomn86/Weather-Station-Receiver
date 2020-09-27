import pickle


class PacketSaver():

    @staticmethod
    def SaveDataForSubscription(packet):
        with open(f"{packet.deviceId}.tmp", "wb") as tmpFile:
            pickle.dump(packet.payload, tmpFile, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def GetSavedPayloadFromFile(deviceId):
        with open(f"{deviceId}.tmp", "rb") as tmpFile:
            payload = pickle.load(tmpFile)
            return payload
