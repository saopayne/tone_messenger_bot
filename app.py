import sys
import json
import requests
from flask import Flask, request

from url_constants import UrlConstants
from url_constants import EnvConstants
from log_status import StatusType
from watson_analyser import WatsonAnalyzer

__author__ = 'Oyewale Ademola'

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == EnvConstants.fb_page_verify_token:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events

    data = request.get_json()
    logger(data, status=StatusType.INFO)

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    # the facebook ID of the person sending you the message
                    sender_id = messaging_event["sender"]["id"]
                    # the recipient's ID, which should be your page's facebook ID
                    recipient_id = messaging_event["recipient"]["id"]
                    # the message's text
                    message_text = messaging_event["message"]["text"]
                    # analyse the text from fb with Watson to determine the mood
                    watson_analyze = WatsonAnalyzer()
                    results = watson_analyze.analyze_tone(text=message_text)
                    if results:
                        watson_analyze.display_results(results)  # show what it looks like
                        # based on the mood, send the appropriate message
                        send_message(sender_id, "roger that!")
                    else:
                        logger("Whoops, something went wrong while analyzing tone of the message", StatusType.ERROR)

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


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
    output = ''
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
