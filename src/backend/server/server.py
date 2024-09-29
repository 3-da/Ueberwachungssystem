from flask import Flask, send_from_directory, request, redirect, url_for

from src.backend.email.send_email import EmailSender

app = Flask(__name__)

@app.route('/')
def hello_root():
    return 'Hello from root!'

# Login-Route, die sowohl GET als auch POST unterstützt
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Abfrage der Formulardaten
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'p123':  # Beispiel für einfache Authentifizierung
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('failed'))

    # Bei GET-Anfrage wird das Login-Formular angezeigt
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

# Fehlerseite bei falschem Login
@app.route('/failed', methods=['GET'])
def failed():
    return send_from_directory('../../frontend', 'failed_login.html')

# Dashboard-Seite
@app.route('/dashboard')
def dashboard():
    return send_from_directory(directory='../../frontend', path='dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
