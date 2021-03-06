from DataUploader import thing_speak_generate_url
from Config import Config
from PacketManager import PacketManager
from Packet import Packet

config = Config("tests/ConfigurationFiles/Config_test.yml")


def test_thingspeak_generate_url_must_return_valid_url():
    packetManager = PacketManager(config)

    validFrame = "S80D4P98012;T3087;H6000;S12;I300;L280000;B419;U077"
    packet = Packet(validFrame)
    payload = packetManager.process_packet(packet)

    url = thing_speak_generate_url(config, payload)

    expected_url = "http://localhost:8080/?api_key=ABCD1234&field1=300" \
        + "&field2=12&field3=4.19&field4=30.87&field5=60.0" \
        + "&field6=1084.84&field7=2800.0&field8=0.77"

    assert expected_url == url
