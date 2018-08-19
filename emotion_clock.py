import RPi.GPIO as GPIO
import time
import random

# pyalsaaudio
import random
import os
import alsaaudio, time, audioop

#import distance

def get_microphone():
    microphone = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK, cardindex=1)
    microphone.setchannels(1)
    #microphone.setrate(44100)
    microphone.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    microphone.setperiodsize(160)
    return microphone

def is_silence(sound):
    try:
        return audioop.max(sound, 2) < 1200
    except:
        return True #False

def listen():
    sounds = []
    print 'listening'
    #play_from_file('im_listening.wav')
    microphone = get_microphone()
    # Read data from device
    begin = time.time()
    while True:
        l,sound = microphone.read()
        if l:
            if not is_silence(sound) and (time.time() - begin) > 0.5:
                break
            #sounds.append(sound)
    return sounds

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    listen()
    print "got"
    p.ChangeDutyCycle(5+random.random()*12)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
