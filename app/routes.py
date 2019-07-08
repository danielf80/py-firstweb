from flask import url_for
from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    rqstname = request.args.get('name', default = '?', type = str)
    return render_template('home.html', name=rqstname)


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('base.html', name=name)
