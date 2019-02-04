from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def courses(name):
    return 'Courses:{}'.format(name)

if __name__ == '__main__':
    app.run()
