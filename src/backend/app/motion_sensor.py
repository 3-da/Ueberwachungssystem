import RPi.GPIO as GPIO


class MotionSensor:
    def __init__(self):
        self.__motion_bcm = int(21)
        self.__motion_detected = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__motion_bcm, GPIO.IN)

    def set_motion_status(self):
        self.__motion_detected = GPIO.input(self.__motion_bcm)

    def get_motion_status(self):
        return self.__motion_detected

    def cleanup(self):
        self.__motion_detected = False
        GPIO.cleanup()