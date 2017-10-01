import json

import requests

from url_constants import UrlConstants
from url_constants import EnvConstants

__author__ = 'Oyewale Ademola'


class WatsonAnalyzer:

    def analyze_tone(self, text):
        watson_username = EnvConstants.watson_username
        watson_password = EnvConstants.watson_password
        headers = {"content-type": "text/plain"}
        data = text
        try:
            requestObject = requests.post(UrlConstants.URL_WATSON, auth=(watson_username, watson_password),
                                          headers=headers, data=data)
            return requestObject.text
        except:
            return False

    def display_results(self, data):
        data = json.loads(str(data))
        print(data)
        for i in data['document_tone']['tone_categories']:
            print(i['category_name'])
            print("-" * len(i['category_name']))
            for j in i['tones']:
                print(j['tone_name'].ljust(20), (str(round(j['score'] * 100, 1)) + "%").rjust(10))
            print()
        print()
