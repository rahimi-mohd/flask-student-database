from api import app, db
from flask import render_template, redirect, flash, url_for
from api.forms import StudentForm
from api.models import Student

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Student database")

@app.route('/add_data', methods=["GET", "POST"])
def add_data():
    form = StudentForm()
    if form.validate_on_submit():
        std = Student(student_id=form.id.data, name=form.name.data, address=form.address.data, classroom=form.classroom.data)
        db.session.add(std)
        db.session.commit()
        flash(f"Student database updated")
    return render_template("add_data.html", title="Add Student Data", form=form)
