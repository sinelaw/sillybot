# pyalsaaudio
import sys

import alsaaudio, time, audioop

def get_microphone():
    microphone = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK,cardindex=1)
    microphone.setchannels(1)
    microphone.setrate(44100)
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
    return audioop.max(sound, 2) < 1000

def record_stuff(filename):
    # Read data from device
    print 'press enter to start'
    sys.stdin.readline()
    print 'recording until silence'
    microphone = get_microphone()
    sounds = []
    begin = time.time()
    while True:
        l,sound = microphone.read()
        if l:
            if is_silence(sound) and (time.time() - begin > 3):
                break
            if not is_silence(sound):
                sounds.append(sound)

    with open(filename, 'w') as f:
        for sound in sounds:
            f.write(sound)



if __name__ == '__main__':
    record_stuff(*sys.argv[1:])
