import requests


def ThingSpeak(config, payload):
    uploadUrl = config.GetUploadAddress()
    apiKey = config.GetUploadApiKey()

    values = payload['values']
    fields = "&field1=" + values['interval']
    fields += "&field2=" + values['status']
    fields += "&field3=" + values['battery']
    fields += "&field4=" + values['temperature']
    fields += "&field5=" + values['humidity']
    fields += "&field6=" + values['pressure']
    fields += "&field7=" + values['luminosity']
    fields += "&field8=" + values['uvRadiation']

    url = f"{uploadUrl}?api_key={apiKey}{fields}"

    if uploadUrl:
        try:
            requests.get(url)
        except Exception as exception:
            raise exception
