from face_recog import FaceRecognition
import time

class App:
    def __init__(self):
        self.fr = FaceRecognition()

    def start(self):
        self.fr.start_authentication()

        while not self.fr.get_authenticated() and not self.fr.get_system_locked():
            time.sleep(1)

if __name__ == "__main__":
    capture_image = App()
    capture_image.start()