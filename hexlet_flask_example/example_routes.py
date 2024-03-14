from flask import Flask, url_for

app = Flask(__name__)

@app.route('/users/')
def users():
    # Код обработчика
    pass

@app.route('/users/<id>')
def users_page(id):
    # Код обработчика
    pass

@app.route('/')
def index():
    # В функцию передается имя обработчика, а она возвращает url
    url_for('users')
    url_for('users_page', id=3)
    # Остальной код
    pass