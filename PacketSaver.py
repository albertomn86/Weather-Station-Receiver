import pickle
from os import path
from Payload import Payload


class PacketSaver():

    @staticmethod
    def SaveDataForSubscription(packet):
        with open(f"{packet.deviceId}.tmp", "wb") as tmpFile:
            pickle.dump(packet.payload, tmpFile, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def GetSavedPayloadFromFile(deviceId):
        tmpFileName = f"{deviceId}.tmp"
        if path.exists(tmpFileName):
            with open(tmpFileName, "rb") as tmpFile:
                payload = pickle.load(tmpFile)
                return payload
        else:
            return Payload()
