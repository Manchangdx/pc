from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def courses(name):
    return render_template('courses.html', name=name)

@app.route('/test')
def test():
    print(url_for('courses', name='java'))
    return redirect('index')

@app.route('/httptest', methods=['get', 'post'])
def haha():
    if request.method == 'GET':
        print(request.args.get('t'))
        print(request.args.get('q'))
        return 'It is a get request!'
    if request.method == 'POST':
        print(request.form.getlist('Q'))
        return 'It is a post request!'
