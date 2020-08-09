import sys
import os
sys.path.append(os.path.abspath("../"))
from PacketReceiver import PacketReceiver

def test_ValidPacketMustEndWithSharpCharacter():

    packet = "S0;4FD0#"
    sut = PacketReceiver.IsValid(packet)

    assert sut == True


def test_ValidPacketMustStartWithDefinedHeader():

    packet = "S0;4FD0#"
    sut = PacketReceiver.IsValid(packet)

    assert sut == True
