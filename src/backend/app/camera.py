import picamera
import time
import face_recognition
import cv2
import numpy as np
from picamera.array import PiRGBArray

# Specify the path to the known face image
admin_image_path = "/home/it/Ueberwachungssystem/src/backend/app/admin.jpg"

# Load the known face image and encode it only once
admin_image = face_recognition.load_image_file(admin_image_path)
admin_face_encoding = face_recognition.face_encodings(admin_image)[0]

# Set up the PiCamera with a suitable resolution
camera = picamera.PiCamera()
camera.resolution = (640, 480)  # Use a reasonable resolution
camera.framerate = 32
raw_capture = PiRGBArray(camera, size=camera.resolution)

# Allow the camera to warm up briefly (can be set to a lower value or removed)
time.sleep(0.1)

try:
    print("Authentication started")

    # Start the camera preview (optional, for development)
    camera.start_preview()
    time.sleep(1)  # Allow a shorter preview adjustment time

    # Continuously capture frames
    for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
        image = frame.array
        
        # Convert the image from BGR to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        # Check if any faces were found
        recognized = False

        # Loop through each face found in the frame
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces([admin_face_encoding], face_encoding)

            if True in matches:
                print("OK")  # Recognized
                recognized = True
                break  # Stop checking further
            else:
                print("Intruder")  # Not recognized
                recognized = True  # Set to true to exit after the first check
                break  # Stop checking further

        # Display the resulting image in a window (set a manageable size)
        cv2.imshow("Camera Feed", cv2.resize(image, (640, 480)))  # Resize to 640x480

        # Clear the stream for the next frame
        raw_capture.truncate(0)

        # Exit if 'q' is pressed or if a recognition occurred
        if cv2.waitKey(1) & 0xFF == ord('q') or recognized:
            break

except KeyboardInterrupt:
    print("Script interrupted.")
finally:
    # Cleanup
    cv2.destroyAllWindows()
    camera.stop_preview()  # Stop the preview before closing
    camera.close()
