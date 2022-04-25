import requests
import uuid
import json

# Add your key and endpoint
key = "insert_key" #removed personal key on April 24, 2022 (after assignment graded)
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "global"

path = '/translate'
constructed_url = endpoint + path

# Set parameters such as what is the inputted language and desired outputted (translated) language
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

# Translation method
def translate(sentence):
    body = [{'text': sentence}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    # Omit any information other than the translation(s)
    response = request.json()[0]['translations'][0]

    # Extract only the translated text and return it
    return json.dumps(response["text"], sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
