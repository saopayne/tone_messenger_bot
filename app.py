# -*- coding: utf-8 -*-
import sys
import json
import pip._vendor.requests as requests
from flask import Flask, request, session

from url_constants import UrlConstants
from url_constants import EnvConstants
from log_status import StatusType
from watson_analyser import WatsonAnalyzer
from mood import Mood

__author__ = 'Oyewale Ademola'

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "unit9_verify_token":
            print(EnvConstants.fb_page_verify_token)
            print(EnvConstants.fb_page_access_token)
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello Bot!", 200


@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events
    mood = Mood()
    data = request.get_json()
    logger(data, status=StatusType.INFO)
    session["current_mood"] = mood.TONE_NEUTRAL  # store the current mood in session
    default_reply = mood.CONST_DEFAULT_REPLY
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):  # someone sent us a message
                    # the facebook ID of the person sending the bot the message
                    sender_id = messaging_event["sender"]["id"]
                    # the message sent by the user
                    if messaging_event["message"]["text"]:
                        message_text = messaging_event["message"]["text"]
                        # if can be an image or attachment ?
                        message_text = message_text.lower()
                        if message_text == mood.CONST_MOOD:
                            current_mood = session["current_mood"]
                            send_message(sender_id, current_mood)
                        elif message_text in mood.default_messages:
                            send_message(sender_id, default_reply)
                        else:
                            send_response(mood=mood, message_text=message_text, sender_id=sender_id)
                    else:
                        logger("Can't process the message as it is not a text, it can either "
                               "be an attachment or something :) ", StatusType.INFO)
                if messaging_event.get("delivery"):  # delivery confirmation
                    pass
                if messaging_event.get("optin"):  # optin confirmation
                    pass
                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass
    return "OK", 200


def send_response(mood, message_text, sender_id):
    # analyse the text from fb with Watson to determine the mood
    watson_analyze = WatsonAnalyzer()
    results = watson_analyze.analyze_tone(message_text)
    if results:
        mood_tone = watson_analyze.get_emotion_tone(results)  # show what it looks like
        session["current_mood"] = mood_tone  # update the current mood in session
        # based on the mood, send the appropriate message
        mood_level = mood.convert_tone_to_mood(mood_tone)
        message_to_send = mood.get_reply_from_mood(mood_level)
        send_message(sender_id, message_to_send)
    else:
        logger("Whoops, something went wrong while analyzing tone of the message", StatusType.ERROR)


def send_message(recipient_id, message_text):
    logger("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text), StatusType.INFO)

    params = {
        "access_token": EnvConstants.fb_page_access_token
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })

    r = requests.post(UrlConstants.URL_FB_MESSAGES, params=params, headers=headers, data=data)
    if r.status_code != 200:
        logger(r.status_code, StatusType.ERROR)
        logger(r.text, StatusType.ERROR)


def logger(message, status):
    output = ""
    if status == StatusType.ERROR:
        output = "ERROR:" + str(message) + ": Status-> {type}".format(type=status)
    elif status == StatusType.DEBUG:
        output = "DEBUG:" + str(message) + ": Status-> {type}".format(type=status)
    elif status == StatusType.INFO:
        output = "INFO:" + str(message) + ": Status-> {type}".format(type=status)
    print(output)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
