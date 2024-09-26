import requests

print("Sending email...")

def send_simple_message():
    try:
        response = requests.post(
            "https://api.mailgun.net/v3/sandboxe954099bd4e64c7c8ddd82c63ca98cff.mailgun.org/messages",
            auth=("api", "022dbae044044fd27bb55dfadeb2089b-1b5736a5-b75091e4"),
            data={"from": "Raum K360 <noreply@überwachungssystem.de>",
                  "to": "test@darijanavric.dev",
                  "subject": "Einbruch!",
                  "text": "Bewegung erkannt!"})
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    send_simple_message()