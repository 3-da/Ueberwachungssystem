from flask import Flask, send_from_directory, render_template, request, redirect, url_for, session
from src.backend.app.send_email import EmailSender
from src.backend.database.add_admins import HandleAdmins
from src.backend.app.app import App

# from src.backend.database.database import session, Admin

server = Flask(__name__, template_folder='../../frontend', static_folder='../../frontend/static')
server.secret_key = '1234'

auth_error = {
    "username": None,
    "password": None
}

logged_in = False

add_admins = HandleAdmins()

@server.route('/')
def index():
    return render_template('index.html', auth_error=auth_error)


@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin_data = add_admins.login_validation()

        for admin in admin_data:
            if username == admin[0] and password == admin[1]:
                session['logged_in'] = True
                return redirect(url_for('dashboard'))
            else:
                auth_error['username'] = 'Username or password is incorrect'
                auth_error['password'] = 'Username or password is incorrect'
                return redirect(url_for('index', auth_error=auth_error))

@server.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

@server.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('dashboard.html')

@server.route('/add-admin', endpoint='add-admin')
def sign_up():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('add_admin.html')

@server.route('/admin-to-db', methods=['POST'])
def add_admin():
    if not session.get('logged_in'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        image_path = request.form.get('image-path')

        add_admins.add_admins(name, password, email, phone, image_path, False)

        return redirect(url_for('dashboard'))

@server.route('/remove-admin', methods=['GET', 'POST'])
def remove_admin():
    if not session.get('logged_in'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form.get('admin_name')
        print(name)
        add_admins.remove_admin(name)

        return redirect(url_for('dashboard'))

@server.route('/show-admins', endpoint='show-admins')
def show_admins():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    admins = add_admins.get_admins()
    return render_template('show_admins.html', admins=admins)

@server.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('../../frontend/static/css', filename)


@server.route('/email')
def hello_email():
    email_sender = EmailSender()
    email_sender.send_email("Einbruch!", "Bewegung erkannt!")
    return 'Email sent!'

if __name__ == '__main__':
    app = App()
    app.run()
    server.run(debug=True)
