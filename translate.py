import requests
import uuid
import json

# Add your key and endpoint
key = "a647b2fe5c524b8dbccb90fb73e61bb9"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "global"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['ko']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def translate(sentence):
    # You can pass more than one object in body.
    body = [{'text': sentence}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    #response = request.json()[0]['translations'][0]
    response = request.json()[0]['translations'][0]

    return json.dumps(response["text"], sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
