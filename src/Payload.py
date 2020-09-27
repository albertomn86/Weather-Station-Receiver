class Payload(object):

    def __init__(self):
        self.interval = None
        self.status = None
        self.battery = None
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.luminosity = None
        self.uvRadiation = None

    def GetValues(self):
        values = {}
        values['interval'] = self.interval
        values['status'] = self.status
        values['battery'] = self.battery
        values['temperature'] = self.temperature
        values['humidity'] = self.humidity
        values['pressure'] = self.pressure
        values['luminosity'] = self.luminosity
        values['uvRadiation'] = self.uvRadiation

        return values

    def KeepValues(self, values):
        if 'I' not in values:
            self.interval = None
        if 'S' not in values:
            self.status = None
        if 'B' not in values:
            self.battery = None
        if 'T' not in values:
            self.temperature = None
        if 'H' not in values:
            self.humidity = None
        if 'P' not in values:
            self.pressure = None
        if 'L' not in values:
            self.luminosity = None
        if 'U' not in values:
            self.uvRadiation = None
