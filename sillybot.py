# pyalsaaudio
import random
import os
import alsaaudio, time, audioop

def get_microphone():
    microphone = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
    microphone.setchannels(1)
    microphone.setrate(8000)
    microphone.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    microphone.setperiodsize(160)
    return microphone


# Open the device in playback mode.
speaker = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
speaker.setchannels(1)
speaker.setrate(8000)
speaker.setformat(alsaaudio.PCM_FORMAT_S16_LE)
speaker.setperiodsize(160)

def is_silence(sound):
    return audioop.max(sound, 2) < 900

actions = ['listen', 'play_back', 'say_something']

def listen():
    sounds = []
    microphone = get_microphone()
    # Read data from device
    print 'listening'
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

def say_something():
    sound_names = os.listdir('sounds')
    picked = random.choice(sound_names)
    print picked
    with open(os.path.join('sounds', picked), 'r') as f:
        speaker.write(f.read())

waiting = 500000
sounds = []
while True:
    action = random.choice(actions)
    if action == 'listen':
        print 'listening'
        sounds.extend(listen())
    elif action == 'play_back':
        print 'playing back'
        play_back(sounds)
        sounds = []
    elif action == 'say_something':
        print 'saying something'
        say_something()
    time.sleep(0.5)

