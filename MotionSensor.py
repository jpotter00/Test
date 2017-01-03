from gpiozero import MotionSensor
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

alert = 1
pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        GPIO.output(14, True)
        print alert
        alert ++
    else:
        GPIO.output(14, False)
        
