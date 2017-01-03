import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
blink = 1

while blink == 1:
    GPIO.output(14, False)
    time.sleep(1)
    GPIO.output(14, True)
    time.sleep(1)

