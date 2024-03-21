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
import os
from .repository import UsersRepository
from .validator import validate
from random import randint


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)

    return render_template(
        'index.html',
        messages=messages,
        )


@app.route('/users')
def users():
    repo = UsersRepository()
    per = 5
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * per
    all_users = repo.content()
    user_at_page = all_users[offset:page * per]
    return render_template(
        'users/index.html',
        page=page,
        users=user_at_page,
    )


@app.route('/users/<id>')
def get_user(id):
    repo = UsersRepository()
    user = repo.find(id)
    if not user:
        return 'Page not found', 404

    return render_template(
        'users/show.html',
        user=user
    )


@app.route('/users/new')
def add_user():
    user = {
        'name': '',
        'email': ''
    }
    errors = {}
    return render_template(
        'users/new.html',
        user=user,
        errors=errors
    )


@app.post('/users')
def set_user():
    repo = UsersRepository()
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        return render_template(
            'users/new.html',
            user=user,
            errors=errors
        ), 422
    user_id = randint(100, 999)
    user['id'] = user_id
    repo.save(user)
    flash('User has been created', 'success')
    return redirect(url_for('index'))


@app.route('/users/<id>/update', methods=['GET', 'POST'])
def update_user(id):
    repo = UsersRepository()
    user = repo.find(id)
    errors = []

    if request.method == 'GET':
        return render_template(
            'users/edit.html',
            user=user,
            errors=errors
        )

    if request.method == 'POST':
        data = request.form.to_dict()
        errors = validate(data)

        if errors:
            return render_template(
                'users/edit.html',
                user=user,
                errors=errors
            ), 422
        user['name'] = data['name']
        user['email'] = data['email']
        repo.delete(user['id'])
        repo.save(user)
        flash('User has been updated', 'success')
        return redirect(url_for('index'))
