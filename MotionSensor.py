from gpiozero import MotionSensor

pir = MotionSensor(2)
#while True:
if pir.motion_detected:
    print ("Motion detected")
