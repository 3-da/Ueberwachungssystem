from flask import Flask

from src.backend.email.send_email import EmailSender

app = Flask(__name__)

@app.route('/')
def hello_root():
    return 'Hello from root!'

@app.route('/data')
def hello_website():
    return 'Hello from website!'

@app.route('/email')
def hello_email():
    email_sender = EmailSender()
    email_sender.send_email("Einbruch!", "Bewegung erkannt!")
    return 'Email sent!'

@app.route('/db')
def hello_db():
    return 'Hello from database!'

if __name__ == '__main__':
    app.run(debug=True)
