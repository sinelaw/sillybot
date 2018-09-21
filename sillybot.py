# pyalsaaudio
import random
import os
import alsaaudio, time, audioop

#import distance
import detect_noise

def init_speaker():
    # Open the device in playback mode.
    speaker = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
    speaker.setchannels(1)
    speaker.setrate(44100)
    speaker.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    speaker.setperiodsize(160)
    return speaker

actions = [
    ('listen',        2),
    ('play_back',     1),
#    ('say_something', 3),
#    ('do_nothing',    4),
]

def listen(speaker):
    sounds = []
    print 'listening'
    play_from_file(speaker, 'im_listening.wav')
    microphone = detect_noise.get_microphone()
    try:
        while True:
            sound = detect_noise.get_sound(microphone)
            if not detect_noise.is_silence(sound):
                sounds.append(sound)
                break
        print 'heard noise'
        begin = time.time()
        while time.time() - begin < 2:
            sound = detect_noise.get_sound(microphone)
            if not detect_noise.is_silence(sound):
                begin = time.time()
                sounds.append(sound)
        print len(sounds)
        return sounds
    finally:
        microphone.close()

def play_back(speaker, sounds):
    with open('/tmp/out.raw', 'wb') as recording_file:
        for sound in sounds:
            speaker.write(sound)
            recording_file.write(sound)

def play_from_file(speaker, filename):
    with open(os.path.join('sounds', filename), 'r') as f:
        speaker.write(f.read())

def say_something(speaker):
    sound_names = os.listdir('sounds')
    picked = random.choice(sound_names)
    print picked
    play_from_file(speaker, picked)

def choose_action(actions):
    random_number = int(random.random() * 10)
    print 'I got: ', random_number
    base = 0
    for (action, how_often) in actions:
        if random_number < base + how_often:
            return action
        base += how_often

def main():
    speaker = init_speaker()
    sounds = []
    played = False
    index = 0
    while True:
        action, bla = actions[index % len(actions)]
        index += 1
        #action = choose_action(actions)
        print 'I chose: ', action
        if action == 'listen':
            if played:
                sounds = []
            played = False
            sounds.extend(listen(speaker))
        elif action == 'play_back':
            play_back(speaker, sounds)
            played = True
        elif action == 'say_something':
            say_something(speaker)
        elif action == 'do_nothing':
            time.sleep(1)
        #while True:
            #if distance.get() < 100:
            #    break
            #time.sleep(0.5)

if __name__ == '__main__':
    main()
