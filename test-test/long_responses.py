import random

R_EATING = 'I don\'t like eating, I am a bot and I require only electricity.'

def unknown():
    response = ['Could you please re-phrase that?',
                '...',
                'Sound about right.',
                'What does that mean?'][random.randrange(4)]
    return response