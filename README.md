# Weather Station Receiver
![Python application](https://github.com/albertomn86/Weather-Station-Receiver/workflows/Python%20application/badge.svg?branch=master)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=albertomn86_Weather-Station-Receiver&metric=alert_status)](https://sonarcloud.io/dashboard?id=albertomn86_Weather-Station-Receiver)

Weather Station data receiver for RaspberryPi. This application processes the data received from the [weather station](https://github.com/albertomn86/Weather-Station).

## Install
Install PIP:
```
sudo apt install -y python3-pip
```
Install Python packages:
```
pip3 install pyyaml pyserial requests
```

### Enable serial port
The Raspberry Pi serial port is disabled by default. If we run the program, we will get the next error:
```
08.Nov 2020 18:17:58 raspberrypi WS-Receiver: (ERROR) [Errno 2] could not open port /dev/ttyS0: [Errno 2] No such file or directory: '/dev/ttyS0'
```

Tho enable the serial port follow the next steps:

1. Open the configuration menu:
```
sudo raspi-config
```

2. Navigate to **Interfacing Options**.

3. Navigate to **Serial** and answer the questions:

    _Would you like a login shell to be accessible over serial?_
    **No**

    _Would you like the serial port hardware to be enabled?_
    **Yes**

4. Close menu and reboot.
