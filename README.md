# README #

* Facebook Messenger Chat Bot with IBM Tone Analyze API

#### Quick Summary

The goal is to create an emotional Facebook Messenger chat bot.
Depending on whether the user sends it a positive or negative message, it will gradually get happier or sadder, which will determine its responses.
All the responses are generic and simply visualise the mood of the bot.

The bot should also replies with its current mood for a special message "mood".

- Typing `hello, hi, ? and some random greetings` will reply with a default message
- Typing `mood` returns the current mood the bot
- Any other `text` will be analyzed via the IBM tone analyzer api and the tone of the message is decoded which in turn triggers a reply to match the tone.
- The Facebook page is accessible here : https://web.facebook.com/saozillz/

##### Version
0.1

### How do I get set up? ###

* Using Docker

> docker pull saopayne/tone-messenger-bot:latest

* Configuration

- Setup Python
- Open this project in an IDE of your choice

The following environmental variables must be set:
> WATSON_USERNAME=''

> WATSON_PASSWORD=''

> PAGE_ACCESS_TOKEN=''

> PAGE_VERIFY_TOKEN=''

#### Dependencies
- To run, the dependencies in the requirements.txt file have to be installed.
- Run `pip install -r requirements.txt` to install them

#### Deployment instructions
- Deployment was done to Heroku
- To run the app `python app.py`
- Open the page 'https://web.facebook.com/saozillz/'
- Type a message in the message part of the Facebook page

#### Repo owner or admin
- Ademola Oyewale (saopayne@gmail.com)
