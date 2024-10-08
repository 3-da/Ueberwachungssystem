import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MOTION_SENSOR = 21
ROT = 26

GPIO.setup(ROT, GPIO.OUT)
GPIO.setup(MOTION_SENSOR, GPIO.IN)

def light():
    GPIO.output(ROT, True)
    time.sleep(1)
    GPIO.output(ROT, False)
    time.sleep(1)

while True:
    motion = GPIO.input(MOTION_SENSOR)
    print(motion)
    if (motion):
        # light()
        GPIO.output(ROT, True)
    else:
        GPIO.output(ROT, False)
    

