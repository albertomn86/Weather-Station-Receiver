# Weather-Station-Receiver
Weather Station data receiver for RaspberryPi

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
