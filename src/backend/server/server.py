from flask import Flask, send_from_directory, render_template, request, redirect, url_for, session, jsonify
from src.backend.app.send_email import EmailSender
from src.backend.database.add_admins import HandleAdmins
# from src.backend.database.database import session, Admin

app = Flask(__name__, template_folder='../../frontend', static_folder='../../frontend/static')
app.secret_key = '1234'

auth_error = {
    "username": None,
    "password": None
}

logged_in = False

add_admins = HandleAdmins()

@app.route('/')
def index():
    return render_template('index.html', auth_error=auth_error)


@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('dashboard.html')

@app.route('/add-admin', endpoint='add-admin')
def sign_up():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('add_admin.html')

@app.route('/admin-to-db', methods=['POST'])
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

@app.route('/remove-admin', methods=['GET', 'POST'])
def remove_admin():
    if not session.get('logged_in'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form.get('admin_name')
        print(name)
        add_admins.remove_admin(name)

        return redirect(url_for('dashboard'))

@app.route('/show-admins', endpoint='show-admins')
def show_admins():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    admins = add_admins.get_admins()
    return render_template('show_admins.html', admins=admins)

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

# @app.route('/add_admin', methods=['POST'])
# def add_admin():
#     rfid = request.form.get('rfid')
#     password = request.form.get('password')
#     oncall = request.form.get('oncall') == 'on'
#     img = request.form.get('img')
#     name = request.form.get('name')
#     email = request.form.get('email')
#     phone = request.form.get('phone')
#
#     new_admin = Admin(
#         rfid=rfid,
#         password=password,
#         oncall=oncall,
#         img=img,
#         name=name,
#         email=email,
#         phone=phone
#     )
#     session.add(new_admin)
#     session.commit()
#     return jsonify({"message": "New admin added successfully!"}), 201


if __name__ == '__main__':
    app.run(debug=True)
