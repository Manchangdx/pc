from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    course = {
        'python': 'lou+ python',
        'java': 'java base',
        'bigdata': 'spark sql',
        'teacher': 'shixiaolou',
        'is_unique': False,
        'has_tag': True,
        'tags': ['c', 'c++', 'docker']
    }
    return render_template('index.html', course=course)

@app.route('/courses/<name>')
def courses(name):
    return render_template('courses.html', name=name)

@app.route('/test')
def test():
    print(url_for('courses', name='java', _external=True))
    return redirect(url_for('index'))

@app.route('/httptest', methods=['get', 'post'])
def httptest():
    if request.method == 'GET':
        print(request.args.get('t'))
        print(request.args.get('q'))
        return 'It is a get request!'
    if request.method == 'POST':
        print(request.form.getlist('Q'))
        return 'It is a post request!'

if __name__ == '__main__':
    app.run()
