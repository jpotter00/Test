import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(4,GPIO.IN)

alert = 1
try:
    while GPIO.input(4) == True:
            GPIO.output(14, True)
            print alert
            alert = alert + 1
            time.sleep(1)
    while GPIO.input(4) == False:
            GPIO.output(14, False)
        
except KeyboardInterrupt:
    print " Quit "
    GPIO.cleanup()
