# models for CalenPeer
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    events = db.relationship("Event", backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class Event(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(30))
    event_date = db.Column(db.DateTime) #db.DateTime is a python datetime object
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #signifies one to many

