import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
# GPIO.cleanup()
reader = SimpleMFRC522()

GPIO.setwarnings(False)

try:
    print("try")
    id, text = reader.read()
    print(f"ID: {id}")
    print(f"Text: {text.strip()}")

except Exception as e:
    print(f"Fehler: {e}")

finally:
    GPIO.cleanup()