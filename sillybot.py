# pyalsaaudio
import random
import os
import alsaaudio, time, audioop

import distance

def get_microphone():
    microphone = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK, cardindex=1)
    microphone.setchannels(1)
    #microphone.setrate(44100)
    microphone.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    microphone.setperiodsize(160)
    return microphone


# Open the device in playback mode.
speaker = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
speaker.setchannels(1)
speaker.setrate(44100)
speaker.setformat(alsaaudio.PCM_FORMAT_S16_LE)
speaker.setperiodsize(160)

def is_silence(sound):
    try:
        return audioop.max(sound, 2) < 900
    except:
        return False

actions = [
    ('listen',        2),
    ('play_back',     1),
    ('say_something', 3),
    ('do_nothing',    4),
]

def listen():
    sounds = []
    print 'listening'
    play_from_file('im_listening.wav')
    microphone = get_microphone()
    # Read data from device
    begin = time.time()
    while True:
        l,sound = microphone.read()
        if l:
            if is_silence(sound) and (time.time() - begin) > 3:
                break
            sounds.append(sound)
    return sounds

def play_back(sounds):
    for sound in sounds:
        speaker.write(sound)

def play_from_file(filename):
    with open(os.path.join('sounds', filename), 'r') as f:
        speaker.write(f.read())

def say_something():
    sound_names = os.listdir('sounds')
    picked = random.choice(sound_names)
    print picked
    play_from_file(picked)

def choose_action(actions):
    random_number = int(random.random() * 10)
    print 'I got: ', random_number
    base = 0
    for (action, how_often) in actions:
        if random_number < base + how_often:
            return action
        base += how_often

waiting = 500000
sounds = []
played = False
while True:
    action = choose_action(actions)
    print 'I chose: ', action
    if action == 'listen':
        if played:
            sounds = []
        played = False
        sounds.extend(listen())
    elif action == 'play_back':
        play_back(sounds)
        played = True
    elif action == 'say_something':
        say_something()
    elif action == 'do_nothing':
        time.sleep(1)
    while True:
        if distance.get() < 100:
            break
        time.sleep(0.5)
