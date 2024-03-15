from flask import (
    Flask, render_template,
    request, redirect, url_for,
    flash, get_flashed_messages
)
from random import randint
from json import dumps
import os

def validate(data):
    errors = {}
    if not data.get('name') or len(data.get('name')) < 4:  # Используем .get для избежания KeyError
        errors['name'] = "Nickname must be grated 4 characters"
    return errors


app = Flask(__name__)
app.secret_key = "secret_key"


@app.post('/users')
def post_users():
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        return render_template(
            'users/new.html',
            user=user,
            errors=errors
        ), 422
    flash('School has been created', 'success')
    return redirect(url_for('get_user'))


@app.route('/users/new')
def new_user():
    user = {
        'name': '',
        'email': '',
    }
    errors = {}
    return render_template(
        'users/new.html',
        user=user,
        errors=errors
    )
