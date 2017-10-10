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
    template = jinja_env.get_template('hello.html')
    return template.render(name=user_name)

app.run()