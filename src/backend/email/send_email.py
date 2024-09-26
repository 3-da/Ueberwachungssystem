import requests
from dotenv import load_dotenv
import os


def send_simple_message():
    load_dotenv()
    api_key = os.getenv("MAILGUN_API_KEY")
    domain = os.getenv("MAILGUN_DOMAIN")

    try:
        response = requests.post(
            domain,
            auth=("api", api_key),
            data={"from": "Raum K360 <noreply@überwachungssystem.de>",
                  "to": "test@darijanavric.dev",
                  "subject": "Einbruch!",
                  "text": "Bewegung erkannt!"})
        response.raise_for_status()
        print("Email sent!")
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    send_simple_message()