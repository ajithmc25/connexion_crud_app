from connection import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    checked = db.Column(db.Boolean)
    name = db.Column(db.String(125))
    type = db.Column(db.String(125))
    age = db.Column(db.Numeric)
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime)


db.create_all()
