from flask import Flask, send_from_directory, render_template, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from src.backend.email.send_email import EmailSender
from src.backend.db_mock import datenbank

app = Flask(__name__)

@app.route('/')
def hello_root():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = next((user for user in datenbank['admin'] if user['username'] == username), None)

        if user and user['password'] == password:
                return jsonify(success=True, redirect_url=url_for('dashboard'))
        elif user and user['password'] != password:
                return jsonify(success=False, error='Incorrect password')
        elif not user and user['password'] == password:
            return jsonify(success=False, error='User not found')
        else:
            return jsonify(success=False, error='User not found and password incorrect')

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

@app.route('/dashboard')
def dashboard():
    return send_from_directory(directory='../../frontend', path='dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)