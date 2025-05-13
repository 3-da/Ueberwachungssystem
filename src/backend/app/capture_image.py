import picamera
import time
from datetime import datetime

class CaptureImage:
    def __init__(self, image_path=None):
        self.image_path = image_path 

    def capture(self):
        # Set timestamp for image capture
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.image_path = self.image_path or f"/home/it/Dokumente/Raumüberwachung II/Ueberwachungssystem/src/backend/app/breakin_{timestamp}.jpg"

        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(1)
            
            # Capture image
            camera.capture(self.image_path)
            
            print(f"Image saved to {self.image_path} with timestamp {timestamp}")
            
            camera.stop_preview()
            camera.close()

if __name__ == "__main__":
    capture_image = CaptureImage()
    capture_image.capture()