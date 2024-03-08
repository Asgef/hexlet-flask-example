from flask import Flask, request

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.post('/users')
def users():
    return 'Users', 302
