import time
import random

# pyalsaaudio
import random
import os
import alsaaudio, time, audioop

def get_microphone():
    microphone = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK, cardindex=1)
    microphone.setchannels(1)
    #microphone.setrate(44100)
    microphone.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    microphone.setperiodsize(1024)
    return microphone

def is_silence(sound):
    try:
        return audioop.max(sound, 2) < 1200
    except Exception as e:
        print e, repr(sound)
        return True #False

def get_sound(microphone):
    while True:
        l,sound = microphone.read()
        if l > 0: break
    return sound

if __name__ == '__main__':
    m = get_microphone()
    while True:
        s = get_sound(m)
        if is_silence(s): pass
        else: print 'ah'

