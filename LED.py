import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(14, GPIO.OUT)
#GPIO.output(14, True)
#time.sleep(3)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, True)
time.sleep(3)

