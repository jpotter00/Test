import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(4,GPIO.IN)

alert = 1
try:
    while True:
       if GPIO.input(4):
            GPIO.output(14, True)
            time.sleep(0.25)
            GPIO.output(14, False)
            GPIO.output(15, True)
            time.sleep(0.25)
            GPIO.output(15, False)
            print "alert number {}".format(alert)
            alert = alert + 1
            
       else:
           GPIO.output(14, False)
           GPIO.output(14, False)
        
except KeyboardInterrupt:
    print " Quit "
    GPIO.cleanup()
