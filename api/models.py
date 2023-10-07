from api import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(200), index=True)
    address = db.Column(db.String(300), index=True)
    classroom = db.Column(db.String(100), index=True)

    def __repr__(self):
        return f"Name: {self.name}\nClassRoom: {classroom}"
