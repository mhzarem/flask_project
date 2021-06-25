from flask_package.models import students
from flask_package import db
from flask import Blueprint, render_template

add = Blueprint('add', __name__)


@add.route('/add/<user>')
def hello_world(user):
    try:
        db.session.add(students(name=user, city='ali', addr='ali', pin='ali'))
        db.session.commit()
    except:
        print("hey that don't work")

    try:
        p = render_template('add.html')

    except:
        p = F"welcome {user}"
    return render_template('hello.html')
