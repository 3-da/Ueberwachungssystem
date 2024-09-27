import picamera
import time

# Specify the path to save the image
image_path = '/home/it/Ueberwachungssystem/src/backend/app/admin.jpg'  # Adjust the path as needed

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)  # Set the desired resolution
    camera.start_preview()  # Start the camera preview
    time.sleep(5)  # Give the camera some time to adjust

    # Capture the image
    camera.capture(image_path)
    print(f"Image saved to {image_path}")

# Camera and resources are automatically cleaned up by the context manager
