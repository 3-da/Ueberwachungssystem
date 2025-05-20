import RPi.GPIO as GPIO
import time
import tkinter as tk
import threading
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

def show_popup():
    popup = tk.Tk()
    popup.title("Benachrichtigung")

    # Festlegen der Fenstergröße
    window_width = 300
    window_height = 150

    # Bildschirmgröße abrufen
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    # Berechnung der x und y Koordinaten für die mittige Position
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    # Fenstergröße und Position setzen
    popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    label = tk.Label(popup, text="Es wurde eine Bewegung im Raum erkannt!")
    label.pack(pady=10)

    # Fenster automatisch nach 3 Sekunden schließen
    popup.after(3000, popup.destroy)

    popup.mainloop()

while True:
    motion = GPIO.input(MOTION_SENSOR)
    print(motion)
    time.sleep(0.3)

    current_time = time.time()
    if motion and (current_time - last_capture_time >= 6):  # Prüfen, ob 6 Sek vergangen sind
        capture_image = CaptureImage()
        capture_image.capture()
        last_capture_time = current_time  # Aktualisieren der Zeit des letzten Captures
        # light()
        threading.Thread(target=show_popup, daemon=True).start()

        
    
