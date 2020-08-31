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
