import picamera
import time

class CaptureImage:
    def __init__(self):
        self.image_path = '/home/it/Ueberwachungssystem/src/backend/app/admin.jpg'

    def capture(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            camera.start_preview()
            time.sleep(5)

            camera.capture(self.image_path)
            print(f"Image saved to {self.image_path}")

            camera.stop_preview()
            camera.close()

if __name__ == "__main__":
    capture_image = CaptureImage()
    capture_image.capture()