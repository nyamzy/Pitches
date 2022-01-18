from enum import unique
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class Jokes:
#     '''
#     Jokes class to define the objects
#     '''
#     def __init__(self, name, title, joke):
#         self.name = name
#         self.title = title
#         self.joke = joke


# class Product:
#     '''
#     Product class to define the objects
#     '''
#     def __init__(self, name, title, product):
#         self.name = name
#         self.title = title
#         self.product = product


# class Vows:
#     '''
#     Vows class to define the objects
#     '''
#     def __init__(self, name, title, vow):
#         self.name = name
#         self.title = title
#         self.vow = vow



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment_title = db.Column(db.String)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id = pitch_id).all()
        return comments


class Pitches(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(255))
    text = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_category(cls, category):
        pitches = Pitches.query.filter_by(category = category).all()
        return pitches
    

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pitches = db.relationship('Pitches', backref = 'user_pitch', lazy = 'dynamic')
    comment = db.relationship('Comment', backref = 'user_comment', lazy = 'dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'