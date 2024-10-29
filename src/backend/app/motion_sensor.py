import RPi.GPIO as GPIO
import time
# import neopixel

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MOTION_SENSOR = 21
ROT = 26
RGB = 18

# pixels = neopixel.NeoPixel(RGB, 24)

GPIO.setup(ROT, GPIO.OUT)
GPIO.setup(MOTION_SENSOR, GPIO.IN)
GPIO.setup(RGB, GPIO.OUT)

# def set_color(color):
#    pixels.fill(color)
#    pixels.show()


def light():
    GPIO.output(ROT, True)
    time.sleep(0.3)
    GPIO.output(ROT, False)
    time.sleep(0.3)

while True:
    motion = GPIO.input(MOTION_SENSOR)
    print(motion)
    if (motion):
        light()
        # GPIO.output(RGB, True)
        # set_color((255,0,0))
    # else:
        # GPIO.output(RGB, False)
    
