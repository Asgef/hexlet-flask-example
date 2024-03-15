from flask import Flask, render_template
import os
import json

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route('/courses')
def get_courses():
    courses_db_path = os.path.join(
        os.path.dirname(__file__), 'templates', 'courses', 'courses_db.json'
    )
    with open(courses_db_path, 'r') as repo:
        content = repo.read()
        if content:
            courses = json.loads(content)
        else:
            courses = []

    return render_template(
           'courses/new.html',
           courses=courses,
           )


@app.route('/courses/<id>')
def get_course(id):
    courses_db_path = os.path.join(
        os.path.dirname(__file__), 'templates', 'courses', 'courses_db.json'
    )
    with open(courses_db_path, 'r') as repo:
        content = repo.read()
        courses = json.loads(content) if content else []

    # Поиск курса по ID
    course = next((item for item in courses if item.get("id") == id), None)
    if course is None:
        return 'Page not found', 404

    return render_template(
          'courses/show.html',
          course=course,
          )
