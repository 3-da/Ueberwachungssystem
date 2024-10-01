import RPi.GPIO as GPIO


class Lights:
    def __init__(self):
        self.red = int(26)
        self.yellow = int(19)
        self.green = int(13)

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