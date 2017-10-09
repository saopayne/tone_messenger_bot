import json

import pip._vendor.requests as requests

from url_constants import UrlConstants
from url_constants import EnvConstants
from mood import Mood

__author__ = 'Oyewale Ademola'


class WatsonAnalyzer:
    CATEGORY_EMOTION_TONE = "Emotion Tone"
    CATEGORY_WRITING_TONE = "Writing Tone"
    CATEGORY_SOCIAL_TONE = "Social Tone"

    def analyze_tone(self, text):
        """
        Sends a request to IBM tone analyze api and returns the text
        :param text: the message to analyze
        :return: string
        """
        watson_username = EnvConstants.watson_username
        watson_password = EnvConstants.watson_password
        headers = {"content-type": "text/plain"}
        data = text
        try:
            request_object = requests.post(UrlConstants.URL_WATSON, auth=(watson_username, watson_password),
                                           headers=headers, data=data)
            return request_object.text
        except:
            return False

    def get_emotion_tone(self, data):
        """
        Returns the tone with the highest score from watson analyze api result
        :param data: the data from watson analyze
        :return: tone with the highest score
        """
        data = json.loads(str(data))
        tone_dict = dict()
        for category in data["document_tone"]["tone_categories"]:
            # Only interested in the emotion category
            if category["category_name"] == self.CATEGORY_EMOTION_TONE:
                for tone in category["tones"]:
                    if tone["tone_name"] == Mood.TONE_ANGER:
                        tone_dict[Mood.TONE_ANGER] = round(tone["score"] * 100, 1)
                    elif tone["tone_name"] == Mood.TONE_DISGUST:
                        tone_dict[Mood.TONE_DISGUST] = round(tone["score"] * 100, 1)
                    elif tone["tone_name"] == Mood.TONE_FEAR:
                        tone_dict[Mood.TONE_FEAR] = round(tone["score"] * 100, 1)
                    elif tone["tone_name"] == Mood.TONE_JOY:
                        tone_dict[Mood.TONE_JOY] = round(tone["score"] * 100, 1)
                    elif tone["tone_name"] == Mood.TONE_SADNESS:
                        tone_dict[Mood.TONE_SADNESS] = round(tone["score"] * 100, 1)
            max_tone = max(tone_dict, key=lambda k: tone_dict[k])
            # if the score is lower than this, the probability of the max being
            # the tone is ambiguous and tone is assigned Neutral
            if tone_dict[max_tone] < 30:
                return Mood.TONE_NEUTRAL
            return max_tone

    def display_results(self, data):
        """
        Displays the result from tone analyze api in a friendly formatted way
        :param data:
        :return: a formatted display of the result from analyze api
        """
        data = json.loads(str(data))
        print(data)
        for i in data["document_tone"]["tone_categories"]:
            print(i["category_name"])
            print("-" * len(i["category_name"]))
            for j in i["tones"]:
                print(j["tone_name"].ljust(20), (str(round(j["score"] * 100, 1)) + "%").rjust(10))
            print()
        print()

    def analyze_single_text(self, text):
        """
        Returns a list of all tone scores
        :param text:
        :return: list
        """
        json_output = json.loads(str(text))
        # store the values in a list and get the max
        anger = json_output["document_tone"]["tone_categories"][0]["tones"][0]["score"]
        fear = json_output["document_tone"]["tone_categories"][0]["tones"][1]["score"]
        disgust = json_output["document_tone"]["tone_categories"][0]["tones"][2]["score"]
        joy = json_output["document_tone"]["tone_categories"][0]["tones"][3]["score"]
        sadness = json_output["document_tone"]["tone_categories"][0]["tones"][4]["score"]
        # get the highest scored among them
        mood_list = [anger, fear, disgust, joy, sadness]
        return mood_list
