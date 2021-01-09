import requests


def thing_speak_generate_url(config, payload):
    upload_url = config.get_upload_address()
    api_key = config.get_upload_api_key()

    values = payload['values']
    fields = "&field1=" + str(values['interval'])
    fields += "&field2=" + str(values['status'])
    fields += "&field3=" + str(values['battery'])
    fields += "&field4=" + str(values['temperature'])
    fields += "&field5=" + str(values['humidity'])
    fields += "&field6=" + str(values['pressure'])
    fields += "&field7=" + str(values['luminosity'])
    fields += "&field8=" + str(values['uvRadiation'])

    url = f"{upload_url}?api_key={api_key}{fields}"

    return url


def thing_speak_uploader(config, payload):
    url = thing_speak_generate_url(config, payload)
    requests.get(url)
