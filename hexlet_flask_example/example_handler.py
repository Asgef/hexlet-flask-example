from flask import Flask

app = Flask(__name__)


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'


