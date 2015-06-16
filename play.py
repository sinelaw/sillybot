# pyalsaaudio

import alsaaudio, time, audioop


# Open the device in playback mode.
speaker = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
speaker.setchannels(1)
speaker.setrate(8000)
speaker.setformat(alsaaudio.PCM_FORMAT_S16_LE)
speaker.setperiodsize(160)

def is_silence(sound):
    return audioop.max(sound, 2) < 900

def record_stuff(filename):
    with open(filename, 'r') as f:
        speaker.write(f.read())



import sys
if __name__ == '__main__':
    record_stuff(*sys.argv[1:])
