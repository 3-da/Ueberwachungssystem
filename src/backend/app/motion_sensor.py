import RPi.GPIO as GPIO
import time
from capture_image import CaptureImage

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MOTION_SENSOR = 21
ROT = 26
RGB = 18

GPIO.setup(ROT, GPIO.OUT)
GPIO.setup(MOTION_SENSOR, GPIO.IN)
GPIO.setup(RGB, GPIO.OUT)

last_capture_time = 0

def light():
    GPIO.output(ROT, True)
    time.sleep(0.3)
    GPIO.output(ROT, False)
    time.sleep(0.3)

while True:
    motion = GPIO.input(MOTION_SENSOR)
    print(motion)
    time.sleep(0.3)

    current_time = time.time()
    if motion and (current_time - last_capture_time >= 6):  # Prüfen, ob 6 Sek vergangen sind
        light()
        capture_image = CaptureImage()
        capture_image.capture()
        last_capture_time = current_time  # Aktualisieren der Zeit des letzten Captures
        
    
