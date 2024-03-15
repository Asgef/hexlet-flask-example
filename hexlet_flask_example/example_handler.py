from flask import Flask, render_template, request

app = Flask(__name__)


users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/users')
def get_users():
    term = request.args.get('term', '')
    filtered_users = list(filter(lambda user: term in user, users))
    return render_template(
        'users/new.html',
        users=filtered_users,
        sarch=term,
    )
