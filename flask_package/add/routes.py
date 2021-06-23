from flask_package.models import students
from flask_package import db
from flask import Blueprint, render_template

add = Blueprint('add', __name__)


@add.route('/add/<user>')
def hello_world(user):
    db.session.add(students(name=user, city='ali', addr='ali', pin='ali'))
    db.session.commit()
    return "render_template('add.html')"