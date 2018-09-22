# pyalsaaudio

import alsaaudio, time, audioop

def open_speaker():
    # Open the device in playback mode.
    speaker = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
    speaker.setchannels(1)
    speaker.setrate(44100)
    speaker.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    speaker.setperiodsize(160)
    return speaker

def is_silence(sound):
    return audioop.max(sound, 2) < 900

def record_stuff(filename):
    print "initing..."
    speaker = open_speaker()
    print "inited"
    with open(filename, 'r') as f:
        speaker.write(f.read())

import sys
if __name__ == '__main__':
    record_stuff(*sys.argv[1:])
