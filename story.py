import time
import random
import espeak.espeak

def synth(text):
    print text
    espeak.espeak.synth(text)
    while espeak.espeak.is_playing():
        time.sleep(0.2)

openings = [
    'once upon a time',
    'yesterday',
    'when I was a baby',
    ]

creatures = [
    'cat',
    'cow',
    'dragon',
    'mouse',
    'monkey',
    ]

adjectives = [
    'blue',
    'hairy',
    'enormous',
    'tiny',
    'weird',
    'hungry',
    'sleepy',
    ]

verbs = [
    'jumped',
    'ate',
    'punched',
    'licked',
    'sniffed',
    'looked at',
    ]

times = [
    'before',
    'after',
    'while',
    ]

def creature():
    return random.choice(adjectives) + ' ' + random.choice(creatures)

def generate():
    espeak.espeak.set_parameter(espeak.espeak.Parameter.Rate, 130)
    opening = random.choice(openings)
    v = random.choice(verbs)
    c1 = creature()
    c2 = creature()
    synth(' '.join([opening, 'a', c1, v, 'a', c2, '.']))
    time.sleep(0.5)
    synth(' '.join([random.choice(times), 'it happened, the', c2, random.choice(verbs), 'the', c1, 'instead']))

if __name__ == '__main__':
    generate()
