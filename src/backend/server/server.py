from flask import Flask, send_from_directory, render_template, request, redirect, url_for
from src.backend.app.send_email import EmailSender
from src.backend.database.db_mock import datenbank

app = Flask(__name__, template_folder='../../frontend', static_folder='../../frontend/static')

auth_error = {
    "username": None,
    "password": None
}

@app.route('/')
def index():

    return render_template('index.html', auth_error=auth_error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        auth_error['username'] = username != 'admin'
        auth_error['password'] = password != 'p123'

        if not auth_error['username'] and not auth_error['password']:
            return redirect(url_for('dashboard'))
        return redirect(url_for('index', auth_error=auth_error))


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


@app.route('/dashboard')
def dashboard():
    return send_from_directory(directory='../../frontend', path='dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
