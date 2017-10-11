from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    user_name = request.form['user-name']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    if not user_name:
        username_error += 'You must fill in the username field. '
    elif len(user_name) < 3:
        username_error += 'Your username must be at least 3 characters long. '
    if not password:
        password_error += 'You must fill in the password field. '
    elif len(password) < 3:
        password_error += 'Your password must be at least 3 characters long. '
    if not verify_password:
        verify_error += 'You must fill in the verify password field. '
    elif password != verify_password:
        verify_error += 'Your passwords do not match. '
    if ' ' in user_name:
        username_error += 'Your username cannot contain a space. '
    if ' ' in password:
        password_error += 'Your password cannot contain a space. '
    if len(user_name) > 20:
        username_error += 'Your username cannot be more than 20 characters long. '
    if len(password) > 20:
        password_error += 'Your password cannot be more than 20 characters long. '
    if email:
        if len(email) < 3:
            email_error += 'An email must contain at least 3 characters. '
        if len(email) > 20:
            email_error += 'An email may not contain more than 20 characters. '
        if email.count('.') != 1:
            email_error += 'An email must contain one period. '
        if email.count('@') != 1:
            email_error += 'An email must contain one @ sign. '
    if email_error:
        email = ''
    if username_error:
        user_name = ''
    if username_error or password_error or verify_error or email_error:
        template = jinja_env.get_template('signup.html')
        return template.render(username_error = username_error, password_error = password_error, 
            verify_error = verify_error, email_error = email_error, 
            user_name = user_name, email = email)
    else: 
        template = jinja_env.get_template('hello.html')
        return template.render(name=user_name)

app.run()