from flask import Flask, send_from_directory, render_template, request, redirect, url_for, session, jsonify
from src.backend.app.send_email import EmailSender
# from src.backend.database.database import Admin, Entrie, Breakin, Error, OnCallDuty, session

app = Flask(__name__, template_folder='../../frontend', static_folder='../../frontend/static')
app.secret_key = '1234'

auth_error = {
    "username": None,
    "password": None
}

logged_in = False

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
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        return redirect(url_for('index', auth_error=auth_error))

@app.route('/signup', endpoint='sign_up')
def sign_up():
    return render_template('sign_up.html')


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




@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
