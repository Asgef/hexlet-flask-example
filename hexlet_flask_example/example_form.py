from flask import (
    Flask, render_template,
    request, redirect, url_for,
    flash, get_flashed_messages
)
from random import randint
from json import dumps
import os


app = Flask(__name__)
app.secret_key = "secret_key"


@app.post('/users')
def users_post():
    user_db_path = os.path.join(os.path.dirname(__file__), 'templates', 'users', 'user_db')
    with open(user_db_path, 'a') as repo:
        user = request.form.to_dict()
        id = randint(100, 999)
        user['id'] = id
        repo.write(dumps(user))
        flash('New user added', 'success')
    return redirect(url_for('users_new'), code=302)


@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            }
    messages = get_flashed_messages(with_categories=True)
    print(messages)

    return render_template(
        'users/new.html',
        user=user,
        messages=messages
    )
