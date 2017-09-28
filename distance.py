import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ECHO=4
TRIG=25
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

#print "Waiting For Sensor To Settle"

#while True:

def get():
    time.sleep(1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    pulse_end = pulse_start
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    #print pulse_duration
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "Distance:",distance,"cm"
    return distance

def cleanup():
    GPIO.cleanup()
