import RPi.GPIO as GPIO


class DoorSensor:
    def __init__(self):
        self.__door_bcm = int(23)
        self.__door_closed = True

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__door_bcm, GPIO.IN)

    def set_door_status(self):
        self.__door_closed = GPIO.input(self.__door_bcm)

    def get_door_status(self):
        return self.__door_closed

    def cleanup(self):
        self.__door_closed = True
        GPIO.cleanup()