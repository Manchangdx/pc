from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def courses(name):
    return render_template('courses.html', coursename=name)

if __name__ == '__main__':
    app.run()
