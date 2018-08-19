import time
import random
import RPi.GPIO as GPIO

import detect_noise

pins = [18, 23]

def func():
    GPIO.setmode(GPIO.BCM)
    microphone = detect_noise.get_microphone()
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in pins:
        GPIO.output(pin, 0)
    while True:
        sound = detect_noise.get_sound(microphone)
        if detect_noise.is_silence(sound):
            time.sleep(0.1)
            for pin in pins:
                GPIO.output(pin, 0)
            continue
        pin = random.choice(pins)
        if random.random() > 0.5:
            GPIO.output(pin, 1)
        else:
            GPIO.output(pin, 0)
        time.sleep(random.random())

func()
