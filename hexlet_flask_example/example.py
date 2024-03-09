from flask import Flask, render_template

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route('/users/<id>')
def users(id):

    return render_template(
        'index.html',
        name=id,
    )


@app.route('/courses/<id>')
def courses(id):

    return render_template(
        'show.html',
        id=id,
    )
