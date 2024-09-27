from flask import Flask, send_from_directory

from src.backend.email.send_email import EmailSender

app = Flask(__name__)

@app.route('/')
def hello_root():
    return 'Hello from root!'

@app.route('/data')
def serve_website():
    return send_from_directory('../../frontend', 'index.html')

@app.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('../../frontend/static/css', filename)

@app.route('/static/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('../../frontend/static/js', filename)

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
