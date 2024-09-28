import RPi.GPIO as GPIO
import time


class Lights:
    def __init__(self, red,yellow,green):
        self.red = int(red)
        self.yellow = int(yellow)
        self.green = int(green)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.yellow, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)

        self.all_off()

    def red_on(self):
        GPIO.output(self.red, GPIO.HIGH)
    
    def red_off(self):
        GPIO.output(self.red, GPIO.LOW)

    def yellow_on(self):
        GPIO.output(self.yellow, GPIO.HIGH)
    
    def yellow_off(self):
        GPIO.output(self.yellow, GPIO.LOW)

    def green_on(self):
        GPIO.output(self.green, GPIO.HIGH)
    
    def green_off(self):
        GPIO.output(self.green, GPIO.LOW)

    def all_off(self):
        self.red_off()
        self.yellow_off()
        self.green_off()

    def cleanup(self):
        self.all_off()
        GPIO.cleanup()