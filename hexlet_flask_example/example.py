from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    get_flashed_messages
)
from random import randint
from json import dumps
import os
from .repository import UsersRepository
from .validator import validate


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)

    return render_template(
        'index.html',
        messages=messages
        )


@app.post('/users')
def users_post():
    repo = UsersRepository()
    user = request.form.to_dict()
    user_id = randint(100, 999)
    user['id'] = user_id
    repo.data_write(dumps(user))
    flash('User Added', 'success')

    return redirect(url_for('index'), code=302)


@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            }

    return render_template(
        'users/new.html',
        user=user
    )
