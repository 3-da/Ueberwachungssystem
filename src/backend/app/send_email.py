import requests
from dotenv import load_dotenv
import os


class EmailSender:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MAILGUN_API_KEY")
        self.domain = os.getenv("MAILGUN_DOMAIN")

    def send_email(self, subject, text):
        try:
            response = requests.post(
                self.domain,
                auth=("api", self.api_key),
                data={"from": "Raum K360 <noreply@überwachungssystem.de>",
                      "to": "test@darijanavric.dev",
                      "subject": subject,
                      "text": text
                      })
            response.raise_for_status()
            print("Email sent!")
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


if __name__ == '__main__':
    email_sender = EmailSender()
    email_sender.send_email("Einbruch!", "Bewegung erkannt!")
