import time
import face_recognition
import cv2
import numpy as np
import picamera
from picamera.array import PiRGBArray
from lights import Lights

class FaceRecognition:
    def __init__(self):
        self.lights = Lights(26, 19, 13)

        self.admin_image_path = "/home/it/Ueberwachungssystem/src/backend/app/admin.jpg"
        self.admin_image = face_recognition.load_image_file(self.admin_image_path)

        # Encodes image to NumPy array and extracts the first face encoding
        self.admin_face_encoding = face_recognition.face_encodings(self.admin_image)[0]
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32

        # Captures raw image in NumPy format
        self.raw_capture = PiRGBArray(self.camera, size=self.camera.resolution)

        # Camera warm up
        time.sleep(0.1)

    def authenticate(self):
        failed_attempts = 0

        for frame in self.camera.capture_continuous(self.raw_capture, format="bgr", use_video_port=True):
            recognized = False
            image = frame.array

            # Takes the image (NumPy in BGR=blue, green, red format) and converts it to RGB red, green, blue format compatible with face_recognition
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Detects all faces in the image and returns their locations as a list of tuples (top, right, bottom, left)
            face_locations = face_recognition.face_locations(rgb_image)
            face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

            for face_encoding in face_encodings:
                # Compares the face encoding with the admin face encoding and returns a list of True/False values
                matches = face_recognition.compare_faces([self.admin_face_encoding], face_encoding)

                if True in matches:
                    print("Authentication successful")
                    self.lights.green_on()
                    time.sleep(3)
                    self.lights.green_off()
                    recognized = True
                    self.lights.cleanup()
                    break

            if not recognized:
                failed_attempts += 1
                print("Authentication failed, trying again...")
                self.lights.yellow_on()
                time.sleep(3)
                self.lights.yellow_off()

                if failed_attempts >= 3:
                    print("System locked")
                    self.lights.red_on()
                    time.sleep(5)
                    self.lights.red_off()
                    self.lights.cleanup()
                    break  # Exit the loop after 3 failed attempts
            else:
                break  # Exit loop on success

            # Clear the stream for the next frame
            self.raw_capture.truncate(0)

            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def start_authentication(self):
        try:
            self.authenticate()
        except KeyboardInterrupt:
            print("Script interrupted.")
        finally:
            # Cleanup
            cv2.destroyAllWindows()
            self.camera.close()

if __name__ == "__main__":
    face_recognition = FaceRecognition()
    face_recognition.start_authentication()