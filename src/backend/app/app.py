from control_unit import ControlUnit
from door_sensor import DoorSensor
from motion_sensor import MotionSensor
from lights import Lights
import threading
import time

class App:
    def __init__(self):
        self.control_unit = ControlUnit()
        self.door_sensor = DoorSensor()
        self.motion_sensor = MotionSensor()
        self.lights = Lights()

        self.run()

    def control_unit_task(self):
        while True:
            self.control_unit.set_system_status()

    def door_sensor_task(self):
        while True:
            self.door_sensor.set_door_status()

            if self.control_unit.get_system_status() and not self.door_sensor.get_door_status():
                self.lights.yellow_on()
            else:
                self.lights.yellow_off()

    def motion_sensor_task(self):
        while True:
            self.motion_sensor.set_motion_status()

            if self.control_unit.get_system_status() and not self.motion_sensor.get_motion_status():
                self.lights.yellow_on()
                time.sleep(0.5)
                self.lights.yellow_off()
                time.sleep(0.5)
            else:
                self.lights.yellow_off()

    def run(self):
        threading.Thread(target=self.control_unit_task).start()
        threading.Thread(target=self.door_sensor_task).start()
        threading.Thread(target=self.motion_sensor_task).start()

    def stop(self):
        self.control_unit.cleanup()
        self.door_sensor.cleanup()
        self.motion_sensor.cleanup()
        self.lights.cleanup()