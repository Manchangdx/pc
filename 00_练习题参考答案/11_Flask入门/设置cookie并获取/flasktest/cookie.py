from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie', methods=['post'])
def setcookie():
    user = request.form.get('name')
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('name', user)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('name')
    return '<h1>Welcome, {}</h1>'.format(name)
