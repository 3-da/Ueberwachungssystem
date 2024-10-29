import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

DOOR_SENSOR = 23
ROT = 26

GPIO.setup(DOOR_SENSOR, GPIO.IN)
GPIO.setup(ROT, GPIO.OUT)

def light():
    GPIO.output(ROT, True)
    time.sleep(0.3)
    GPIO.output(ROT, False)
    time.sleep(0.3)

while True:
    door = GPIO.input(DOOR_SENSOR)
    print(door)
    if door == 0:
        light()
        # GPIO.output(RGB, True)
        # set_color((255,0,0))
    # else:
        # GPIO.output(RGB, False)