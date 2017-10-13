FROM ubuntu:16.04

MAINTAINER Oyewale Ademola "saopayne@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage iiDocker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# Make the port publicly accessible as Flask runs on port 5000
EXPOSE 5000

# Set the environment variables in the container launched from an image
ENV PAGE_ACCESS_TOKEN EAAB8jMhzYzQBAMoAtAUfLcA6P7TQqhzOOlp55EhvG9eDxzqCYGZBwJJRsKMZAir3znMeG6z7bRG0c33TRgRZBafb0mERNMyZCZBZA7ZCzZCv8gZABMx0YdNLy9ZC5RLVW0SZARGaLKW99Q46ZA35gR56Wh1ddFQx2hql0vJ6w0riJmDf4DGsxSSL8c9n 
ENV PAGE_VERIFY_TOKEN unit9_verify_token

ENV WATSON_USERNAME 1322070a-87a2-4433-b7b3-e18f5db99f69

ENV WATSON_PASSWORD kEOwPPlIhUSp

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
