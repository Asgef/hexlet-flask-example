from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    # redirect,
    # url_for,
    # flash,
    # get_flashed_messages
)
import os
from .repository import UsersRepository
# from .validator import validate


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    # messages = get_flashed_messages(with_categories=True)

    return render_template(
        'index.html',
        # messages=messages
        )


@app.route('/users')
def users():
    repo = UsersRepository()
    per = 5
    page = request.args.get('page', 1, type=int)
    offset = (page -1) * per
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
    print(user)
    if not user:
        return 'Page not found', 404

    return render_template(
        'users/show.html',
        user=user
    )
