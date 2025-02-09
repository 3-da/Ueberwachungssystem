import RPi.GPIO as GPIO


class Lights:
    def __init__(self):
        self.red_bcm = int(26)
        self.yellow_bcm = int(19)
        self.green_bcm = int(13)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red_bcm, GPIO.OUT)
        GPIO.setup(self.yellow_bcm, GPIO.OUT)
        GPIO.setup(self.green_bcm, GPIO.OUT)

        self.all_off()

    def red_on(self):
        GPIO.output(self.red_bcm, GPIO.HIGH)

    def red_off(self):
        GPIO.output(self.red_bcm, GPIO.LOW)

    def yellow_on(self):
        GPIO.output(self.yellow_bcm, GPIO.HIGH)

    def yellow_off(self):
        GPIO.output(self.yellow_bcm, GPIO.LOW)

    def green_on(self):
        GPIO.output(self.green_bcm, GPIO.HIGH)

    def green_off(self):
        GPIO.output(self.green_bcm, GPIO.LOW)

    def all_off(self):
        self.red_off()
        self.yellow_off()
        self.green_off()

    def cleanup(self):
        self.all_off()
        GPIO.cleanup()
