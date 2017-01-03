import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(4,GPIO.IN)

alert = 1
try:
    while GPIO.input(4)== True:
            GPIO.output(14, True)
            print alert
            alert = alert + 1
        
except KeyboardInterrupt:
    print " Quit "
    GPIO.cleanup()
