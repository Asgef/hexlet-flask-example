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
from .validator import validate
import json
from hexlet_flask_example import user_cookies


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
    per = 5
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * per
    all_usr_json = request.cookies.get('all_usr', '[]')
    all_usr = json.loads(all_usr_json)
    user_at_page = all_usr[offset:page * per]
    return render_template(
        'users/index.html',
        page=page,
        users=user_at_page,
    )


@app.route('/users/<int:id>')
def get_user(id):
    all_usr_json = request.cookies.get('all_usr', '[]')
    all_usr = json.loads(all_usr_json)
    user = user_cookies.find(all_usr, id)
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


@app.route('/users', methods=['POST'])
def set_user():
    all_usr_json = request.cookies.get('all_usr', '[]')
    all_usr = json.loads(all_usr_json)
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        return render_template(
            'users/new.html',
            user=user,
            errors=errors
        ), 422
    user_id = user_cookies.gen_usr_id(all_usr)
    user['id'] = user_id
    all_usr.append(user)
    encoded_users = json.dumps(all_usr)
    response = redirect(url_for('index'))
    response.set_cookie('all_usr', encoded_users)
    flash('User has been created', 'success')
    return response


@app.route('/users/<int:id>/update', methods=['GET', 'POST'])
def update_user(id):
    all_usr_json = request.cookies.get('all_usr', '[]')
    all_usr = json.loads(all_usr_json)
    user = user_cookies.find(all_usr, id)
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
        all_usr = user_cookies.delete(all_usr, id)
        all_usr.append(user)
        encoded_users = json.dumps(all_usr)
        response = redirect(url_for('index'))
        response.set_cookie('all_usr', encoded_users)
        flash('User has been updated', 'success')
        return response


@app.route('/users/<int:id>/delete', methods=['POST'])
def delete_user(id):
    all_usr_json = request.cookies.get('all_usr', '[]')
    all_usr = json.loads(all_usr_json)
    all_usr = user_cookies.delete(all_usr, id)
    print(f'print {all_usr}')
    encoded_users = json.dumps(all_usr)
    response = redirect(url_for('index'))
    response.set_cookie('all_usr', encoded_users)
    flash('User has been deleted', 'success')
    return response
