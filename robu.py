import time
import random
import RPi.GPIO as GPIO

import story
import detect_noise

pins = [18, 23]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in pins:
        GPIO.output(pin, 0)

def stop():
    for pin in pins:
        GPIO.output(pin, 0)
    time.sleep(1)

def tell_story():
    story.generate()

def move():
    cycle = 0.2
    speed = 1
    directions = [
        ('forward', (1,1)),
        ('left', (0,1)),
        ('right', (1,0))]
    name, direction = directions[0]
    microphone = detect_noise.get_microphone()
    for i in xrange(5):
        sound = detect_noise.get_sound(microphone)
        if not detect_noise.is_silence(sound):
            name, direction = random.choice(directions)
            speed = random.random() * 0.5 + 0.5
        print direction, speed
        story.synth(name)
        begin = time.time()
        while time.time() - begin < 1:
            for pin, val in zip(pins, direction):
                GPIO.output(pin, val)
            time.sleep(cycle * speed)

            for pin, val in zip(pins, direction):
                GPIO.output(pin, 0)
            time.sleep(cycle * (1 - speed))

actions = [
    tell_story,
    stop,
    move
]


def func():
    setup()
    time.sleep(5)
    stop()
    while True:
        action = random.choice(actions)
        action()
        time.sleep(1)


if __name__ == '__main__':
    func()
