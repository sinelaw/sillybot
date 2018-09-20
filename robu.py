import time
import random
import RPi.GPIO as GPIO

import detect_noise

pins = [18, 23]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in pins:
        GPIO.output(pin, 0)

def func():
    microphone = detect_noise.get_microphone()
    setup()
    time.sleep(5)
    while True:
        sound = detect_noise.get_sound(microphone)
        if detect_noise.is_silence(sound):
        #    time.sleep(0.1)
            for pin in pins:
                GPIO.output(pin, 0)
            continue
        directions = [(0,0),(0,1),(1,0),(1,1)]
        dir = random.choice(directions)
        start = time.time()
        cycle = 0.2
        target_freq = random.random()
        freq = 0.1
        while freq < target_freq:
            freq += target_freq / 2 
            #print freq
            for i in xrange(2):
                for pin, val in zip(pins, dir):
                    GPIO.output(pin, val)
                time.sleep(cycle * freq)
                for pin, val in zip(pins, dir):
                    GPIO.output(pin, 0)
                time.sleep(cycle * (1 - freq))

if __name__ == '__main__':
    func()

