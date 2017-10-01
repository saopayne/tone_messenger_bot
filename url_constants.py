import os

__author__ = 'Oyewale Ademola'


class UrlConstants:
    URL_FB_MESSAGES = "https://graph.facebook.com/v2.6/me/messages"
    URL_WATSON = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21'


class EnvConstants:
    watson_username = os.environ["WATSON_USERNAME"]
    watson_password = os.environ["WATSON_PASSWORD"]
    fb_page_access_token = os.environ["PAGE_ACCESS_TOKEN"]
    fb_page_verify_token = os.environ["VERIFY_TOKEN"]
