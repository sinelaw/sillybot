# pyalsaaudio

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

def record_stuff(filename):
    microphone = get_microphone()
    # Read data from device
    print 'listening'
    begin = time.time()
    while True:
        l,sound = microphone.read()
        if l:
            if is_silence(sound):
                break
            sounds.append(sound)

    with open(filename, 'w') as f:
        for sound in sounds:
            f.write(sound)



import sys
if sys.name == '__main__':
    record_stuff(*sys.argv[1:])
