import picamera
import time
import face_recognition
import cv2
import numpy as np
from picamera.array import PiRGBArray
from lights import Lights

lights = Lights(26,19,13)

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

# Allow the camera to warm up briefly
time.sleep(0.1)

try:
    print("Authentication started")

    # Start the camera preview
    camera.start_preview()
    time.sleep(1)  # Allow a shorter preview adjustment time

    failed_attempts = 0  # Counter for failed attempts

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
                print("Successful")  # Recognized successfully
                lights.green_on()
                time.sleep(3)
                lights.green_off()
                recognized = True
                lights.cleanup()
                break  # Stop checking further

        # If no face was recognized
        if not recognized:
            failed_attempts += 1
            print("Authentication failed, trying again...")
            lights.yellow_on()
            time.sleep(3)
            lights.yellow_off()

            if failed_attempts >= 3:
                print("System locked")
                lights.red_on()
                time.sleep(5)
                lights.red_off()
                lights.cleanup()
                break  # Exit the loop after 3 failed attempts
        else:
            # Exit if recognized successfully
            break  # Exit the loop immediately on success

        # Display the resulting image in a window
        cv2.imshow("Camera Feed", cv2.resize(image, (640, 480)))  # Resize to 640x480

        # Clear the stream for the next frame
        raw_capture.truncate(0)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Script interrupted.")
finally:
    # Cleanup
    cv2.destroyAllWindows()
    camera.stop_preview()  # Stop the preview before closing
    camera.close()
