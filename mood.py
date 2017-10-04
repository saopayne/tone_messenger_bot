# -*- coding: utf-8 -*-
import random

__author__ = 'Oyewale Ademola'


class Mood:

    MOOD_LEVEL_POSITIVE = 'positive'
    MOOD_LEVEL_NEGATIVE = 'negative'
    MOOD_LEVEL_NEUTRAL = 'neutral'
    MOOD_LEVEL_UNKNOWN = 'unknown'

    TONE_ANGER = 'Anger'
    TONE_DISGUST = 'Disgust'
    TONE_FEAR = 'Fear'
    TONE_JOY = 'Joy'
    TONE_SADNESS = 'Sadness'
    TONE_NEUTRAL = 'Neutral'

    messages_positive_mood = [
        'It\'s a beautiful day down here, what are you upto?',
        'Stay happy! Do you care to check out some of the things we might possibly suggest?',
        'Interesting. What\'s on your mind today?',
        'Banging your head against the wall burns 150 calories an hour. Wanna try :)',
        'Billy goats urinate on their own heads to smell more attractive to females'
    ]
    messages_negative_mood = [
        'That\'s a pretty sad thing. Be happy. Better times are ahead',
        'A flock of crows is known as murder :) I hope you giggle at this :)',
        'Life is beautiful and open your heart to the beauty',
        'Uh oh uh oh, I don\'t know what it means but you aren\'t alone. You are loved.',
        'You are awesome, this will pass. Stay happy!'
    ]
    messages_neutral_mood = [
        'What do you want to talk about today?', 'Here is a game you can play->',
        'Cherophobia is the fear of fun. I hope you don\'t have the fear',
        'Bananas are curved because they grow towards the sun',
        'Heart attacks are more likely to happen on a Monday. Have a stress free Monday :)',
        'King Henry VIII slept with a gigantic axe behind him'
    ]

    def get_mood_list(self, mood):
        """
        Get the list of the mood corresponding to the level
        :param mood: text
        :rtype: list
        """
        if mood == self.MOOD_LEVEL_NEGATIVE:
            mood_list = self.messages_negative_mood
        elif mood == self.MOOD_LEVEL_POSITIVE:
            mood_list = self.messages_positive_mood
        elif mood == self.MOOD_LEVEL_NEUTRAL:
            mood_list = self.messages_neutral_mood
        else:
            mood_list = self.messages_neutral_mood
        return mood_list

    def get_reply_from_mood(self, mood):
        """
        Gets a random message in the mood list given a mood type
        :param mood : text
        :rtype: string
        """
        mood_list = self.get_mood_list(mood)
        random_message = random.choice(mood_list)
        return random_message

    def convert_tone_to_mood(self, tone):
        """
        Converts a tone to a mood level (positive, negative, neutral)
        :param tone:
        :return:
        """
        if tone == self.TONE_ANGER or tone == self.TONE_SADNESS or tone == self.TONE_DISGUST:
            return self.MOOD_LEVEL_NEGATIVE
        elif tone == self.TONE_JOY:
            return self.MOOD_LEVEL_POSITIVE
        elif tone == self.TONE_NEUTRAL or tone == self.TONE_FEAR:
            return self.MOOD_LEVEL_NEUTRAL
        else:
            return self.MOOD_LEVEL_UNKNOWN
