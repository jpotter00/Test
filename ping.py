import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(14,GPIO.OUT)

ip = input("Input IP")
GPIO.output(14, True)


try:
    while True:
        if GPIO.input(4):
            ping ip -l 65527
            print "pinging " + ip
            
            
    
    
