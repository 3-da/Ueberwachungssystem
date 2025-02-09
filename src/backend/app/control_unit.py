import RPi.GPIO as GPIO


class ControlUnit:
    def __init__(self):
        self.__system_bcm = int(20)
        self.__system_armed = True

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__system_bcm, GPIO.IN)

    def set_system_status(self):
        system_button = GPIO.input(self.__system_bcm)

        if not system_button:
            self.__system_armed = not self.__system_armed

    def get_system_status(self):
        return self.__system_armed

    def cleanup(self):
        self.__system_armed = True
        GPIO.cleanup()