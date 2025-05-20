# from lights import Lights
import time

class App:
    # def __init__(self):
        # self.lights = Lights()
        # self.lights.red_on()
        # time.sleep(2)
        # self.lights.red_off()

    def start(self):
        self.fr.start_authentication()

        while not self.fr.get_authenticated() and not self.fr.get_system_locked():
            time.sleep(1)

if __name__ == "__main__":
    capture_image = App()
    # capture_image.start()