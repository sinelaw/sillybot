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
        for pin in pins:
            GPIO.output(pin, 0)
        if random.random() > 0.02:
            continue
        cycle = 0.2
        directions = [(0,0), (0,1), (1,0), (1,1)]
        direction = directions[0]
        while True:
            sound = detect_noise.get_sound(microphone)
            if not detect_noise.is_silence(sound):
                direction = random.choice(directions)
                speed = random.random() * 0.5 + 0.5

            for pin, val in zip(pins, direction):
                GPIO.output(pin, val)
            time.sleep(cycle * speed)

            for pin, val in zip(pins, direction):
                GPIO.output(pin, 0)
            time.sleep(cycle * (1 - speed))

if __name__ == '__main__':
    func()
