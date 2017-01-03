from gpiozero import MotionSensor
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        GPIO.output(14, True)
    else:
        GPIO.output(14, False)
        
