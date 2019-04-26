from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def courses(name):
    return render_template('courses.html', name=name)

@app.route('/test')
def test():
    print(url_for('courses', name='java', _external=True))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
