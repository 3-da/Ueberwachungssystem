import picamera
from datetime import datetime
from backend.app.save_image import SaveImage

class CaptureImage:
    def __init__(self, image_path=None):
        self.image_path = image_path 

    def capture(self):
        # Set timestamp for image capture
        timestamp_obj   = datetime.now()
        timestamp_str   = timestamp_obj.strftime("%Y-%m-%d_%H-%M-%S")
        self.image_path = self.image_path or f"/home/it/Dokumente/Raumüberwachung_II/Ueberwachungssystem/src/backend/app/img/breakin_{timestamp_str}.jpg"

        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.start_preview(fullscreen=False, window = (1150,100,640,480))
            
            # Capture image
            camera.capture(self.image_path)
            
            print(f"Image saved to {self.image_path} with timestamp {timestamp_obj}")

            # Save image and timestamp in database table
            save_image = SaveImage()
            save_image.add_entry(self.image_path, timestamp_obj)
            
            camera.stop_preview()
            camera.close()

if __name__ == "__main__":
    capture_image = CaptureImage()
    capture_image.capture()