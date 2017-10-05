# README #

* Unit9 Facebook Messenger Chat Bot

#### Quick Summary

The goal of this task is to create an emotional Facebook Messenger chat bot.
Depending on whether the user sends it a positive or negative message, it will gradually get happier or sadder, which will determine its responses.
All the responses are generic and simply visualise the mood of the bot.

The bot should also reply with its current mood for a special message "mood".

- Typing `hello, hi, ? and some random greetings` will reply with a default message
- Typing `mood` returns the current mood the bot
- Any other `text` will be analyzed via the IBM tone analyzer api and the tone of the message is decoded which in turn triggers a reply to match the tone.
- The Facebook page is accessible here : https://web.facebook.com/saozillz/

##### Version
0.1

### How do I get set up? ###

* Configuration

- Setup Python
- Open this project in an IDE of your choice

The following environmental variables must be set:
> WATSON_USERNAME=1322070a-87a2-4433-b7b3-e18f5db99f69
> WATSON_PASSWORD=kEOwPPlIhUSp
> PAGE_ACCESS_TOKEN=EAAB8jMhzYzQBAMoAtAUfLcA6P7TQqhzOOlp55EhvG9eDxzqCYGZBwJJRsKMZAir3znMeG6z7bRG0c33TRgRZBafb0mERNMyZCZBZA7ZCzZCv8gZABMx0YdNLy9ZC5RLVW0SZARGaLKW99Q46ZA35gR56Wh1ddFQx2hql0vJ6w0riJmDf4DGsxSSL8c9n
> PAGE_VERIFY_TOKEN=unit9_verify_token

#### Dependencies
- To run, the dependencies in the requirements.txt file have to be installed.
- Run `pip install requirements.txt` to install them

#### Deployment instructions
- Deployment was done to Heroku
- To run the app `python app.py`
- Open the page 'https://web.facebook.com/saozillz/'
- Type a message in the message part of the Facebook page
- App is currently accessible on 'https://unit9-bot.herokuapp.com/'

#### Repo owner or admin
- Ademola Oyewale (saopayne@gmail.com)
